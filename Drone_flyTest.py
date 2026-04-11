from pysimverse import Drone

import cv2

import keyboard

import time

# Initialize the drone

drone = Drone()

drone.connect()

drone.streamon()

# Variables for drone state

fb_speed = 0  # Forward/Backward speed

lr_speed = 0  # Left/Right speed

ud_speed = 0  # Up/Down speed

yaw_speed = 0  # Yaw (rotation) speed

speed = 50  # Movement speed

screenshot_effect_duration = 0.3  # Duration of flash effect (seconds)

last_screenshot_time = 0  # Store time of last screenshot

drone.take_off()

try:

    while True:

        frame, is_success = drone.get_frame()

        if is_success:
            frame = cv2.resize(frame, (360, 240))

            cv2.imshow("Image", frame)

            cv2.waitKey(1)

            # Reset speeds

        fb_speed = 0

        lr_speed = 0

        ud_speed = 0

        yaw_speed = 0

        camera_angle = 0

        # Check for key presses and update speeds

        if keyboard.is_pressed('w'):  # Move forward

            fb_speed = speed

        if keyboard.is_pressed('s'):  # Move backward

            fb_speed = -speed

        if keyboard.is_pressed('a'):  # Move left

            lr_speed = -speed

        if keyboard.is_pressed('d'):  # Move right

            lr_speed = speed

        if keyboard.is_pressed('i'):  # Move up

            ud_speed = speed

        if keyboard.is_pressed('k'):  # Move down

            ud_speed = -speed

        if keyboard.is_pressed('j'):  # Rotate left (yaw)

            yaw_speed = -0.5

        if keyboard.is_pressed('l'):  # Rotate right (yaw)

            yaw_speed = 0.5

        if keyboard.is_pressed('t'):  # Rotate up (yaw)

            camera_angle = -10

        if keyboard.is_pressed('g'):  # Rotate down (yaw)

            camera_angle = 10

        # Capture a screenshot when z is pressed

        if keyboard.is_pressed("z"):
            timestamp = time.strftime("%Y%m%d_%H%M%S")

            filename = f"screenshot_{timestamp}.jpg"

            cv2.imwrite(filename, frame)

            print(f"Screenshot saved as {filename}")

        # Send RC control commands to the drone

        drone.send_rc_control(lr_speed, fb_speed, ud_speed, yaw_speed)

        # Small delay to avoid overwhelming the system

        time.sleep(0.05)



except KeyboardInterrupt:

    print("Drone landed safely. Exiting...")