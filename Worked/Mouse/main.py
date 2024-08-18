import pyautogui
import time

# Function to move the mouse pointer at a certain interval
def keep_mouse_active(interval=60):
    """
    Keeps the mouse pointer moving at a specified interval.

    :param interval: Time in seconds between each move.
    """
    while True:
        x, y = pyautogui.position()  # Get current mouse position
        pyautogui.moveTo(x + 1, y + 1, duration=0.1)  # Move mouse slightly
        pyautogui.moveTo(x, y, duration=0.1)  # Move it back to the original position
        time.sleep(interval)  # Wait for the specified interval

# Example usage
keep_mouse_active(interval=30)                