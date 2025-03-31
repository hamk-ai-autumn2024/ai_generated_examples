# db.py - Database Layer
import sqlite3
from typing import List, Tuple, Optional

class WarehouseDB:
    def __init__(self, db_name: str = "warehouse.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.initialize()

    def initialize(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        # Create table if it doesn't exist
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL,
            amount INTEGER NOT NULL
        )
        ''')
        
        # Create indexes for efficient queries
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_name ON products (name)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_price ON products (price)')
        
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None

    def add_product(self, name: str, price: int, amount: int) -> bool:
        """Add a new product to the database."""
        try:
            self.cursor.execute(
                'INSERT INTO products (name, price, amount) VALUES (?, ?, ?)',
                (name, price, amount)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"Error adding product: {e}")
            return False

    def update_product(self, name: str, price: int, amount: int) -> bool:
        """Update an existing product."""
        try:
            self.cursor.execute(
                'UPDATE products SET price = ?, amount = ? WHERE name = ?',
                (price, amount, name)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating product: {e}")
            return False

    def delete_product(self, name: str) -> bool:
        """Delete a product by name."""
        try:
            self.cursor.execute('DELETE FROM products WHERE name = ?', (name,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False

    def get_product_by_name(self, name: str) -> Optional[Tuple[str, int, int]]:
        """Get a product by its exact name."""
        try:
            self.cursor.execute('SELECT name, price, amount FROM products WHERE name = ?', (name,))
            result = self.cursor.fetchone()
            return result if result else None
        except Exception as e:
            print(f"Error getting product: {e}")
            return None

    def find_products_by_partial_name(self, partial_name: str) -> List[Tuple[str, int, int]]:
        """Find products by partial name (case insensitive)."""
        try:
            self.cursor.execute(
                'SELECT name, price, amount FROM products WHERE name LIKE ? COLLATE NOCASE',
                (f'%{partial_name}%',)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error finding products: {e}")
            return []

    def get_all_products_by_name(self) -> List[Tuple[str, int, int]]:
        """Get all products ordered by name."""
        try:
            self.cursor.execute('SELECT name, price, amount FROM products ORDER BY name ASC')
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error getting products by name: {e}")
            return []

    def get_all_products_by_price(self) -> List[Tuple[str, int, int]]:
        """Get all products ordered by price."""
        try:
            self.cursor.execute('SELECT name, price, amount FROM products ORDER BY price ASC')
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error getting products by price: {e}")
            return []


# warehouse.py - Business Logic Layer
class Warehouse:
    def __init__(self, db_name: str = "warehouse.db"):
        self.db = WarehouseDB(db_name)

    def close(self):
        """Close the database connection."""
        self.db.close()

    def add_product(self, name: str, price_euros: float, amount: int) -> bool:
        """
        Add a new product to the warehouse.
        
        Args:
            name: The name of the product
            price_euros: The price in euros (will be converted to cents)
            amount: The quantity in stock
            
        Returns:
            bool: True if the product was added successfully, False otherwise
        """
        if not name or price_euros < 0 or amount < 0:
            return False
        
        # Convert euros to cents
        price_cents = int(price_euros * 100)
        
        return self.db.add_product(name, price_cents, amount)

    def update_product(self, name: str, price_euros: float, amount: int) -> bool:
        """
        Update an existing product.
        
        Args:
            name: The name of the product
            price_euros: The new price in euros (will be converted to cents)
            amount: The new quantity in stock
            
        Returns:
            bool: True if the product was updated successfully, False otherwise
        """
        if not name or price_euros < 0 or amount < 0:
            return False
        
        # Convert euros to cents
        price_cents = int(price_euros * 100)
        
        return self.db.update_product(name, price_cents, amount)

    def delete_product(self, name: str) -> bool:
        """Delete a product by name."""
        if not name:
            return False
        
        return self.db.delete_product(name)

    def get_product_by_name(self, name: str) -> Optional[Tuple[str, float, int]]:
        """Get a product by its exact name, with price converted to euros."""
        result = self.db.get_product_by_name(name)
        if result:
            name, price_cents, amount = result
            return name, price_cents / 100, amount
        return None

    def find_products_by_partial_name(self, partial_name: str) -> List[Tuple[str, float, int]]:
        """Find products by partial name, with prices converted to euros."""
        results = self.db.find_products_by_partial_name(partial_name)
        return [(name, price_cents / 100, amount) for name, price_cents, amount in results]

    def get_all_products_by_name(self) -> List[Tuple[str, float, int]]:
        """Get all products ordered by name, with prices converted to euros."""
        results = self.db.get_all_products_by_name()
        return [(name, price_cents / 100, amount) for name, price_cents, amount in results]

    def get_all_products_by_price(self) -> List[Tuple[str, float, int]]:
        """Get all products ordered by price, with prices converted to euros."""
        results = self.db.get_all_products_by_price()
        return [(name, price_cents / 100, amount) for name, price_cents, amount in results]


# ui.py - User Interface Layer
class WarehouseUI:
    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse

    def display_menu(self):
        """Display the main menu."""
        print("\n===== Warehouse Management System =====")
        print("1. Add a new product")
        print("2. Modify existing product")
        print("3. Delete existing product")
        print("4. List products in alphabetical order")
        print("5. List products by price")
        print("6. Find product by partial name")
        print("7. Exit and save")
        print("======================================")

    def get_menu_choice(self) -> int:
        """Get the user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")

    def confirm_action(self, action: str) -> bool:
        """Confirm an action with the user."""
        while True:
            response = input(f"Do you want to {action}? (y/n): ").lower()
            if response in ('y', 'yes'):
                return True
            elif response in ('n', 'no'):
                return False
            else:
                print("Please enter 'y' or 'n'.")

    def add_product(self):
        """Add a new product."""
        print("\n--- Add New Product ---")
        while True:
            name = input("Enter product name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            
            product = self.warehouse.get_product_by_name(name)
            if product:
                print(f"A product with name '{name}' already exists.")
                continue
                
            break
            
        while True:
            try:
                price = float(input("Enter price in euros: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                amount = int(input("Enter amount: "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")
        
        if self.warehouse.add_product(name, price, amount):
            print(f"Product '{name}' added successfully.")
        else:
            print("Failed to add product. Please try again.")

    def modify_product(self):
        """Modify an existing product."""
        print("\n--- Modify Existing Product ---")
        name = input("Enter the name of the product to modify: ").strip()
        
        product = self.warehouse.get_product_by_name(name)
        if not product:
            print(f"No product found with name '{name}'.")
            return
        
        print(f"Product found: {product[0]}, Price: €{product[1]:.2f}, Amount: {product[2]}")
                
        while True:
            try:
                price = float(input(f"Enter new price (current: €{product[1]:.2f}): "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                amount = int(input(f"Enter new amount (current: {product[2]}): "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")

        if not self.confirm_action("modify this product"):
            print("Operation cancelled.")
            return

        if self.warehouse.update_product(name, price, amount):
            print(f"Product '{name}' updated successfully.")
        else:
            print(f"Failed to update product '{name}'.")

    def delete_product(self):
        """Delete an existing product."""
        print("\n--- Delete Existing Product ---")
        name = input("Enter the name of the product to delete: ").strip()
        
        product = self.warehouse.get_product_by_name(name)
        if not product:
            print(f"No product found with name '{name}'.")
            return
        
        print(f"Product found: {product[0]}, Price: €{product[1]:.2f}, Amount: {product[2]}")
        
        if not self.confirm_action("delete this product"):
            print("Operation cancelled.")
            return
        
        if self.warehouse.delete_product(name):
            print(f"Product '{name}' deleted successfully.")
        else:
            print(f"Failed to delete product '{name}'.")

    def list_products_by_name(self):
        """List all products in alphabetical order."""
        print("\n--- Products in Alphabetical Order ---")
        products = self.warehouse.get_all_products_by_name()
        self._display_products(products)

    def list_products_by_price(self):
        """List all products by price."""
        print("\n--- Products by Price ---")
        products = self.warehouse.get_all_products_by_price()
        self._display_products(products)

    def find_products(self):
        """Find products by partial name."""
        print("\n--- Find Products ---")
        partial_name = input("Enter part of the product name: ").strip()
        
        products = self.warehouse.find_products_by_partial_name(partial_name)
        if products:
            print(f"\nFound {len(products)} product(s) matching '{partial_name}':")
            self._display_products(products)
        else:
            print(f"No products found matching '{partial_name}'.")

    def _display_products(self, products: List[Tuple[str, float, int]]):
        """Display a list of products."""
        if not products:
            print("No products found.")
            return
        
        print(f"\n{'Name':<30} {'Price':>10} {'Amount':>10}")
        print("-" * 50)
        for name, price, amount in products:
            print(f"{name:<30} €{price:>9.2f} {amount:>10}")
        print(f"\nTotal: {len(products)} products")

    def run(self):
        """Run the UI."""
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.modify_product()
            elif choice == 3:
                self.delete_product()
            elif choice == 4:
                self.list_products_by_name()
            elif choice == 5:
                self.list_products_by_price()
            elif choice == 6:
                self.find_products()
            elif choice == 7:
                print("Exiting and saving database...")
                break


# main.py - Main Application
def main():
    """Main entry point for the warehouse application."""
    try:
        warehouse = Warehouse()
        ui = WarehouseUI(warehouse)
        ui.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            warehouse.close()
        except:
            pass
        print("Application terminated.")

if __name__ == "__main__":
    main()