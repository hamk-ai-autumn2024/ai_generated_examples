## ai_generated_examples

Here you can find many examples, which are generated using different AI tools, mostly using GitHub Copilot.
As little human interaction as possible has been done to generate these.

## Prompts:

# Number guessing Game. (number_game.py) gpt-4o
Generate number guessing game in Python. Generate random integer 1-100. If the user guesses too low, prompt accordingly. If the user guesses too high, prompt accordingly. When the user guesses correctly, also tell how many attempts it took.

# Number guessing Game. (number_game_tkinter.py) gpt-4o
(same as above prompt)
use Tkinter for GUI

# Home Page for a Company (home_page.html) Claude 3.5 Sonnet
generate home page for gym, include title "Riihimäki Genius Gym", slogan, some text about gym facilities and opening hours and placeholder for image.

# Candy Crush Saga-alike game (candy_crush_clone.html) gpt-o3-mini
Generate Candy Crush clone in JS using HTML5 canvas. Aim for nice looking colorful graphics and use animations to show when connect-3 happens. Make sure this connect-3 game show the points and there is a way to restart the game. In the beginng of the game check 3-matches. Show score on screen. Do NOT use alert or prompt. Embed all JavaScript into one HTML5 file and make it mobile friendly as well.

# Platform game (platform_game.html) - Claude 3.5 Sonnet
Generate using a platform jumping game in JavaScript, using HTML5 canvas. The game should have:
- 3 levels, first being very easy, next being easy and the last being medium difficulty
- A score counter and display of level number.
- Game character can be controlled using arrow keys or WASD. Space, up arrow or A jumps. Using Super Mario style jumping mechanism and be able to jump through platforms from below and fall down through them when pressing down or S.
- There should be gold coins to collect in each level. You must collect enough coins to reach the goal post
- There should be a way to restart the game.
- Do NOT use alert or prompt

# Calculator (calculator.html) Claude 3.5 Sonnet
generate a kawaii calculator using HTML5 and JS

# Calculator (calculator2.html) DeepSeek-R1-Distilled-Llama3.3-70B under Croq
generate a kawaii calculator using HTML5 and JS

# Painting program (paint.html) Claude 3.5 Sonnet
Generate painting program similar to Microsoft Paint using JavaScript and HTML5 Canvas. The painting program should have at least the following features:
- draw with mouse
- eraser tool with mouse (draw with background color)
- adjust the line width
- fill closed area starting from the point clicked
- change the drawing color and fill color
- draw filled rectangles by dragging the mouse from left upper corner
- empty the canvas
Make sure you handle drag events correctly, so they don't trigger browser default actions.

# TODO Web app (todo.html) Claude 3.5 Sonnet
Create responsive mobile friendly HTML5 page, which has TODO app made using latest JavaScript.
The TODO app must have the following functionality:
1. Text field to add new TODO items. Pressing enter key on this field should trigger the form.
2. Button with "add" text to add new TODO items. Pressing add button should add TODO items into a ul-li list.
3. Clicking an item in the ul-li list should mark event as completed, by applying strike-through text style on the text.
4. There should also be a button next to each item with the Unicode character "❌" and that should remove the TODO item.
5. There should be button with text "Clear all" to remove all TODO events and update the list accordingly.

Make sure the app doesn't have XSS vulnerability and follows the best practices.

# TODO Web app (todo_localstorage.html) o3-mini
(same as above, but also with:)
Store the TODO items into localStorage and delete them from localStorage when needed.

# Warehouse JS app (warehouse4.html) Claude 3.5 Sonnet
Create responsive mobile friendly HTML5 page, which has warehouse app made using latest JavaScript.

The warehouse data is stored in an inventory object, which can contain multiple item objects. Each item object has:
- name (must be unique)
- price (in cents)
- amount (how many of items of this name exist in the warehouse)

The inventory object is stored in localStorage.

The warehouse app must have the following functionality:
1. ability to add new items into the warehouse
2. ability to adjust price and amount of items, but inputting the item name, new price and new amount
3. ability to remove items from the warehouse
4. display all the warehouse items automatically and this display updated every time new items are added, adjusted or deleted

Separate the user interface from the actual code, which manipulates the warehouse items.

Create a robust solution with error checking:
- Give appropriate error messages if use tries to adjust amount of item for an item, which doesn't exist:
- Check that item price and amount are appropriate

Aim for compact UI. Do not waste screen estate for large headers.

Do NOT use alert or prompt, but use HTML5 forms instead. Make sure the app doesn't have XSS vulnerability and follows the best practices.

# BMI app (bmi.html) Claude 3.5 Sonnet
Create responsive mobile friendly HTML5 page, which has BMI and health app made using latest JavaScript.
The UI should look beautiful and slick.

The app should have following features:
- input fields for height (cm) and weight (kg), button to calculate BMI based on those
- calculate body mass index (BMI), display it in 1 decimal precision and also give verbal description of it
- give diet & fitness tips for healthier BMI for those who are not within normal range

The app should be robust and display appropriate error messages in case user gives wrong input. Do NOT use alert or prompt, but use HTML5 forms instead.



