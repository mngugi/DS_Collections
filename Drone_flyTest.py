from pysimverse import Drone
import cv2
import time
from pynput import keyboard

# ------------------------
# Keyboard handling
# ------------------------
keys = set()

def on_press(key):
    try:
        keys.add(key.char)
    except:
        pass

def on_release(key):
    try:
        keys.discard(key.char)
    except:
        pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# ------------------------
# Drone setup
# ------------------------
drone = Drone()
drone.connect()

drone.streamon()
time.sleep(2)  # IMPORTANT: allow stream to initialize

drone.take_off()
time.sleep(2)

speed = 50
fail_count = 0

try:
    while True:

        # ------------------------
        # Get frame
        # ------------------------
        frame, is_success = drone.get_frame()

        if not is_success or frame is None:
            fail_count += 1
            print(f"Frame decode failed: {fail_count}")

            # Auto-restart stream if too many failures
            if fail_count > 15:
                print("Restarting video stream...")
                drone.streamoff()
                time.sleep(1)
                drone.streamon()
                time.sleep(2)
                fail_count = 0

            time.sleep(0.05)
            continue

        fail_count = 0  # reset on success

        # ------------------------
        # Display frame
        # ------------------------
        frame = cv2.resize(frame, (360, 240))
        cv2.imshow("Drone Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # ------------------------
        # Reset speeds
        # ------------------------
        fb_speed = 0
        lr_speed = 0
        ud_speed = 0
        yaw_speed = 0

        # ------------------------
        # Controls
        # ------------------------
        if 'w' in keys:
            fb_speed = speed
        if 's' in keys:
            fb_speed = -speed
        if 'a' in keys:
            lr_speed = -speed
        if 'd' in keys:
            lr_speed = speed
        if 'i' in keys:
            ud_speed = speed
        if 'k' in keys:
            ud_speed = -speed
        if 'j' in keys:
            yaw_speed = -50
        if 'l' in keys:
            yaw_speed = 50

        # ------------------------
        # Screenshot
        # ------------------------
        if 'z' in keys:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            time.sleep(0.3)  # debounce

        # ------------------------
        # Send RC control
        # ------------------------
        drone.send_rc_control(lr_speed, fb_speed, ud_speed, yaw_speed)

        time.sleep(0.03)

except KeyboardInterrupt:
    print("Landing...")

finally:
    drone.land()
    cv2.destroyAllWindows()