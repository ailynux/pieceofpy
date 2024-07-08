import LCD_1in44
import time
import numpy as np
from PIL import Image, ImageDraw

# Screen dimensions
WIDTH, HEIGHT = 128, 128

# Waveform properties
amplitude = HEIGHT // 4
frequency = 2
speed = 0.1

# Main function to display the waveform animation on the LCD
def main():
    try:
        # Initialize the LCD
        LCD = LCD_1in44.LCD()
        LCD.LCD_Init(LCD_1in44.SCAN_DIR_DFT)
        LCD.LCD_Clear()

        phase = 0  # Initialize phase

        while True:
            # Create a blank image
            image = Image.new("RGB", (WIDTH, HEIGHT), "BLACK")
            draw = ImageDraw.Draw(image)

            # Draw the sine wave
            for x in range(WIDTH):
                y = int(HEIGHT / 2 + amplitude * np.sin(2 * np.pi * frequency * (x / WIDTH) + phase))
                draw.point((x, y), fill="GREEN")

            # Rotate the image 180 degrees
            image = image.rotate(180)

            # Display the image
            LCD.LCD_ShowImage(image, 0, 0)

            # Update the phase to create the moving effect
            phase += speed

            # Short delay to control the speed of the animation
            time.sleep(0.05)
    except KeyboardInterrupt:
        # Clear the LCD on exit
        LCD.LCD_Clear()
        print("Exiting...")

# Entry point
if __name__ == '__main__':
    main()
