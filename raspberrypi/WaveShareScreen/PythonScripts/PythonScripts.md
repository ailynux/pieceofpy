# Implementing Programs on the Waveshare LCD HAT

## Step-by-Step Guide

### 1. Create the Script File
```bash
nano conway_life.py

CTRL+O(the letter) - Saves file 
```
### 2. Add the Following Code
```bash
import LCD_1in44
import time
import numpy as np
from PIL import Image, ImageDraw

# Screen dimensions
WIDTH, HEIGHT = 128, 128

# Game of Life properties
CELL_SIZE = 4
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Initialize the grid with random values
def initialize_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))

# Compute the next generation of the grid
def next_generation(grid):
    new_grid = np.copy(grid)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            live_neighbors = np.sum(grid[max(0, x-1):min(GRID_WIDTH, x+2), max(0, y-1):min(GRID_HEIGHT, y+2)]) - grid[x, y]
            if grid[x, y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if live_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

# Main function to display Conway's Game of Life on the LCD
def main():
    try:
        # Initialize the LCD
        LCD = LCD_1in44.LCD()
        LCD.LCD_Init(LCD_1in44.SCAN_DIR_DFT)
        LCD.LCD_Clear()

        # Initialize the grid
        grid = initialize_grid()

        while True:
            # Create a blank image
            image = Image.new("RGB", (WIDTH, HEIGHT), "BLACK")
            draw = ImageDraw.Draw(image)

            # Draw the cells
            for x in range(GRID_WIDTH):
                for y in range(GRID_HEIGHT):
                    if grid[x, y] == 1:
                        draw.rectangle([x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE - 1, (y + 1) * CELL_SIZE - 1], fill="WHITE")

            # Rotate the image 180 degrees
            image = image.rotate(180)

            # Display the image
            LCD.LCD_ShowImage(image, 0, 0)

            # Compute the next generation
            grid = next_generation(grid)

            # Short delay to control the speed of the animation
            time.sleep(0.1)
    except KeyboardInterrupt:
        # Clear the LCD on exit
        LCD.LCD_Clear()
        print("Exiting...")

# Entry point
if __name__ == '__main__':
    main()
```
### 3. Save and Exit
 - Press Ctrl+X, then Y, then Enter to save and exit the Nano editor.

### 4. Run the Script
```bash
sudo python3 conway_life.py
```
