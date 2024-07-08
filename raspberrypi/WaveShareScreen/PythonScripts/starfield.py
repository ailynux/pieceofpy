import LCD_1in44
import time
import random
from PIL import Image, ImageDraw

# Screen dimensions
WIDTH, HEIGHT = 128, 128

# Starfield properties
NUM_STARS = 100
stars = []

# Initialize stars with random positions and velocities
for _ in range(NUM_STARS):
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    velocity = random.uniform(0.1, 1.5)
    stars.append([x, y, velocity])

# Main function to display the starfield on the LCD
def main():
    try:
        # Initialize the LCD
        LCD = LCD_1in44.LCD()
        LCD.LCD_Init(LCD_1in44.SCAN_DIR_DFT)
        LCD.LCD_Clear()

        while True:
            # Create a blank image
            image = Image.new("RGB", (WIDTH, HEIGHT), "BLACK")
            draw = ImageDraw.Draw(image)

            for star in stars:
                x, y, velocity = star

                # Move the star down the screen
                y += velocity

                # If the star goes off the screen, reset it to the top
                if y >= HEIGHT:
                    y = 0
                    x = random.randint(0, WIDTH - 1)
                    velocity = random.uniform(0.1, 1.5)
                
                # Update the star position
                star[1] = y

                # Draw the star
                draw.point((x, y), fill="WHITE")

            # Rotate the image 180 degrees
            image = image.rotate(180)

            # Display the image
            LCD.LCD_ShowImage(image, 0, 0)

            # Short delay to control the speed of the animation
            time.sleep(0.01)
    except KeyboardInterrupt:
        # Clear the LCD on exit
        LCD.LCD_Clear()
        print("Exiting...")

# Entry point
if __name__ == '__main__':
    main()
