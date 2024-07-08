import LCD_1in44
import time
from PIL import Image, ImageDraw

# Ball properties
ball_radius = 5
ball_color = (255, 0, 0)
ball_speed = [2, 2]  # x, y speeds

# Initialize ball position
ball_position = [ball_radius, ball_radius]

# Main function to display and animate the ball on the LCD
def main():
    try:
        # Initialize the LCD
        LCD = LCD_1in44.LCD()
        LCD.LCD_Init(LCD_1in44.SCAN_DIR_DFT)
        LCD.LCD_Clear()

        while True:
            # Create a blank image
            image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
            draw = ImageDraw.Draw(image)

            # Update ball position
            ball_position[0] += ball_speed[0]
            ball_position[1] += ball_speed[1]

            # Check for collision with the screen edges and bounce
            if ball_position[0] - ball_radius <= 0 or ball_position[0] + ball_radius >= LCD.width:
                ball_speed[0] = -ball_speed[0]
            if ball_position[1] - ball_radius <= 0 or ball_position[1] + ball_radius >= LCD.height:
                ball_speed[1] = -ball_speed[1]

            # Draw the ball
            draw.ellipse(
                (ball_position[0] - ball_radius, ball_position[1] - ball_radius,
                 ball_position[0] + ball_radius, ball_position[1] + ball_radius),
                fill=ball_color
            )

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
