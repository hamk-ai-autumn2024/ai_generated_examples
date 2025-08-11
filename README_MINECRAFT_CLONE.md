# HTML5 Minecraft-like Voxel World

A lightweight, single-file voxel sandbox inspired by Minecraft. Built with HTML5 + modern JavaScript using Three.js modules from a CDN. No build step required.

## Features
- Procedural terrain (grass/dirt/stone layers)
- Break/place blocks with simple raycasting
- Save and load edits using localStorage (P = save, L = load)
- Reset world (R) and UI buttons for Start/Reset
- Pointer lock controls (WASD to move, mouse to look, Space to jump, Shift to sprint)
- Minimal collision with axis-wise sweep for smooth walking
- Inventory with 5 block types (1–5 to switch)

## Controls
- Movement: W A S D
- Jump: Space
- Sprint: Hold Shift
- Place: Right click
- Break: Left click
- Save: P
- Load: L
- Reset: R
- Block hotbar: 1–5

## How to run
Open the `minecraft_clone.html` file directly in a modern browser.

Note: The page imports Three.js modules from `unpkg.com`. If your environment blocks external requests, you can download Three.js locally and update the import URLs.

## Troubleshooting
- If the mouse doesn’t lock, click the Start button in the overlay and allow pointer lock when prompted.
- If performance is low, reduce render resolution by changing the `setPixelRatio` line to `1`.
- If blocks don’t place, ensure you’re not intersecting with the block position (the game avoids placing blocks inside the player).

## License
This example is for educational purposes. Uses Three.js (MIT).
