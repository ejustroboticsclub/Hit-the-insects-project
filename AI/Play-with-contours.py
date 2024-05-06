import numpy as np
import cv2
import pyautogui
import time

def find_ball(image):
    # Define lower and upper bounds for the color of the ball
    H_MIN = 20
    S_MIN = 100
    V_MIN = 100
    H_MAX = 66
    S_MAX = 255
    V_MAX = 255

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only the ball color
    mask = cv2.inRange(hsv, (H_MIN, S_MIN, V_MIN), (H_MAX, S_MAX, V_MAX))

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming the largest contour represents the ball
    if contours:
        c = max(contours, key=cv2.contourArea)
        # Compute the bounding circle of the ball
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        return ((x, y), radius, mask)
    else:
        return None

def distance_to_camera(knownWidth, focalLength, perWidth):
    # Compute and return the distance from the marker to the camera
    return (knownWidth * focalLength) / perWidth

# Initialize the known distance from the camera to the object, which
# in this case is 30cm
KNOWN_DISTANCE = 30  # cm
# Initialize the known object width, which in this case, we assume the ball size is 5cm wide
KNOWN_WIDTH = 5  # cm

# Threshold distance to trigger the cursor movement (in cm)
THRESHOLD_DISTANCE = 20  # cm

# Initialize video capture from default camera (0)
cap = cv2.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Make a copy of the original frame
    frame_with_mask = frame.copy()

    # Detect the ball and get the mask in the frame
    ball_info = find_ball(frame_with_mask)

    if ball_info is not None:
        # Unpack the ball information
        ((ball_x, ball_y), ball_radius, mask) = ball_info

        # Assuming the ball is a circle, calculate the diameter
        ball_diameter = 2 * ball_radius

        # Calculate the focal length using the ball's apparent width
        focalLength = (ball_diameter * KNOWN_DISTANCE) / KNOWN_WIDTH

        # Calculate the distance to the ball
        dist = distance_to_camera(KNOWN_WIDTH, focalLength, ball_diameter)

        # Print ball information in the terminal
        print(f"Ball detected at ({ball_x}, {ball_y}) with radius {ball_radius}px")

        # Move the cursor to the position of the ball if the distance is below the threshold
        if dist < THRESHOLD_DISTANCE:
            # Map the coordinates to the screen resolution
            screen_width, screen_height = pyautogui.size()
            cursor_x = int((ball_x / frame.shape[1]) * screen_width)
            cursor_y = int((ball_y / frame.shape[0]) * screen_height)

            # Move the cursor
            pyautogui.moveTo(cursor_x, cursor_y)

            # Pause for 0.3 seconds
            time.sleep(0.3)

            # Simulate a mouse click at the cursor position
            pyautogui.click()

        # Draw circle around the ball and display "ball"
        cv2.circle(frame_with_mask, (int(ball_x), int(ball_y)), int(ball_radius), (0, 255, 255), 2)
        cv2.putText(frame_with_mask, "Ball", (int(ball_x - ball_radius), int(ball_y) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Show the mask in a separate window
        mask_resized = cv2.resize(mask, (frame.shape[1] // 2, frame.shape[0] // 2))  # Resize mask for display
        cv2.imshow('Mask', mask_resized)

    else:
        # If no ball is detected, show an empty mask
        empty_mask = np.zeros_like(frame)
        empty_mask_resized = cv2.resize(empty_mask, (((frame.shape[1] * 4)//3), (frame.shape[0] * 2)))  # ((Width) and (Height) of the window
        cv2.imshow('Countouring View', empty_mask_resized)

    # Show the original frame
    frame_resized = cv2.resize(frame_with_mask, ((frame.shape[1] * 4)//3, frame.shape[0] * 2))  # ((Width) and (Height) of the window
    cv2.imshow('Real view', frame_resized)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
