import LCD_1in44
import time
import random
from PIL import Image, ImageDraw, ImageFont

# Screen dimensions
WIDTH, HEIGHT = 128, 128

# Matrix effect properties
FONT_SIZE = 10
COLUMNS = WIDTH // FONT_SIZE
ROWS = HEIGHT // FONT_SIZE

# Create a list to hold the vertical position of each column
positions = [random.randint(0, ROWS) for _ in range(COLUMNS)]

# Main function to display the matrix effect on the LCD
def main():
    try:
        # Initialize the LCD
        LCD = LCD_1in44.LCD()
        LCD.LCD_Init(LCD_1in44.SCAN_DIR_DFT)
        LCD.LCD_Clear()

        # Load a font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", FONT_SIZE)

        while True:
            # Create a blank image
            image = Image.new("RGB", (WIDTH, HEIGHT), "BLACK")
            draw = ImageDraw.Draw(image)

            for i in range(COLUMNS):
                # Draw a random number
                number = str(random.randint(0, 9))
                draw.text((i * FONT_SIZE, positions[i] * FONT_SIZE), number, font=font, fill="GREEN")

                # Move the position of the column down
                positions[i] += 1

                # Reset the position if it goes off screen
                if positions[i] * FONT_SIZE >= HEIGHT:
                    positions[i] = 0

            # Rotate the image 180 degrees
            image = image.rotate(180)

            # Display the image
            LCD.LCD_ShowImage(image, 0, 0)

            # Short delay to control the speed of the animation
            time.sleep(0.1)
    except KeyboardInterrupt:
        # Clear the LCD on exit
        LCD.LCD_Clear()
        print("Exiting...")

# Entry point
if __name__ == '__main__':
    main()
