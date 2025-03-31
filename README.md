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
Generate Candy Crush clone in JS using HTML5 canvas. Aim for nice looking colorful graphics and use animations to show when connect-3 happens. Make sure this connect-3 game show the points and there is a way to restart the game. In the beginning of the game check all the 3-matches. Show score on screen. Do NOT use alert or prompt. Embed all JavaScript into one HTML5 file and make it mobile friendly as well. Simple swipe and click the matching elements should both work.

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
Generate a painting app similar to Microsoft Paint using JavaScript and HTML5 Canvas. The painting app should have at least the following features:
- draw with mouse (hold mouse down)
- eraser tool with mouse (draw with background color)
- adjust the line width
- fill closed area starting from the point clicked
- change the drawing color (triggering color selector)
- change the fill color
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

# 3D City (3d_city.html) Claude 3.7 Sonnet
Generate a rustic nice-looking green 3D city where you can move using WASD and arrow keys and jump with space button. Use mouse to control the camera like in most FPS games. Try to include basic collision detection. Pressing R should reset the player to the original position and direction.

Generate all the code in one HTML5 file, using JavaScript. If you use external libraries, link them via CDN.

Now all the houses look similar and there are no roads or elevation. The house roof is floating above the building. Fix these issues. 
1. Roof should be connected the house. House should be connected to the ground.
2. Add roads.
3. Add some hills around the city, potentially blocking player.

# racing Claude 3.7 Sonnet
Generate a top-down view 2D racing game. The car can be controlled using WASD and arrow keys. A/left arrow to turn left and D/right arrow to turn right. W/up arrow should emulate the gas pedal of the car, increasing acceleration until top speed is reached. S/down arrow to should simulate the break pedal of the car. Pressing it should deaccelerate and stop the car. Pressing break longer time e.g. 0.5 seconds while stopped should allow the car to be moved backwards.

The game should begin at the middle of the finish line. The finishing/start line should be perpendicular to the track. The game is measuring how fast the player completed the lap and shows both the all-time best. In order to finish a lap the car must pass through several check points and go over the finish line. The track should be interesting and not a circle. 

The track has 2 kinds of objects to collect:
- coins (and HUD is showing how many coins collected)
- speed boosts (give a 2 second speed boost)

Driving over an item will pick it. Finish a lap should reset all the collective items. Pressing R button will reset the game.

The car should appear in such way that is obvious that which way is front e.g. arrow in the hood of the car pointing towards the direction it moves.

Generate all the code in one HTML5 file, using JavaScript. If you use external libraries, link them via CDN. Do NOT use alert or prompt.

# space shooter Claude 3.7 Sonnet
Generate 2D space shooter game. Make it look cool and retro. The player is controlling a space ship against waves of enemies, which slowly come at it in large numbers.

The ship is controlled as follows:
left arrow/A = move left
right arrow/D = move right
space = shoot
The space ship is limited to stay within the lower part of the screen and cannot go off screen.

Each time the user presses space it shoots a missile, which a bright vertical bar moving up fast. If the missile hits an enemy, the enemy and missile are destroyed. There is 20% of change the enemy drops an item, which slowly sinks down.

Pick up items:
- Heart shape (H), gives 3 health
- Speed boost (S), gives 50% movement speed for 10 seconds.

If enemy manages to hit the player ship, the ship takes 1 hit point damage. The ship originally has 10 hit points.

Finally there is a large boss enemy, which has 50 hit points. It requires 50 hits.

If the player hit points drop to zero, "Game Over" is displayed on screen. If the player defeats the boss, "You win" is displayer on screen. 

Pressing R restarts the game.

Generate all the code in one HTML5 file, using JavaScript. If you use external libraries, link them via CDN. Do NOT use alert or prompt.

# speech_synthesizer.html
Make a speech synthesizer using HTML5 and JavaScript. The responsive and mobile friendly web page should have an input text area and select-option selector for the voices (at minimum English, Spanish, Chinese and more), speech speed and speech frequency setting. Pressing the "Speak" button will utter the input text using Web Speech API.

# warehouse_db.py
Generate a warehouse app using Python and sqlite3 and text based user interface. Separate the logic and user interface completely.

Each warehouse item has the following attributes:
- name (str) = name of the item
- price (int) in cents = price in cents, but rendered as euros (€) in user interface
- amount (int) = how items are currently in the warehouse of the given name

The warehouse app must have the following functionality:

1. Add a new product:
prompt user for name (str), price (float) in euros, amount (int)
automatically convert the price from euros into cents (for internal DB storage)

2. Modify existing product:
- Search product based on name
- If not product of the supplied name was found, tell user there is no product of such name.
- If product was found, prompt user for new price and amount. Otherwise act as "add a new product".
- confirm user yes/no to actually modify or not

3. Delete existing product.
- Search product based on name
- If not product of the supplied name was found, tell user there is no product of such name.
- If product was found, remove it.
- confirm user yes/no to delete

4. List products in ascending alphabetical order.

5. List products in ascending price order.

6. Find product based on partial name. Should be case intensitive.
- e.g. If user searches "saw", he should also find "CHAINSAW".

7. Exit and save results to database.

Include comprehensive error checking. Create indexes for the most widely used listing and search operations (ordered by name and ordered by price).