import pyautogui
import keyboard
import time
from datetime import datetime
import os

SAVE_DIR = "captured_screens"

def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def take_screenshot():
    ensure_save_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    full_path = os.path.join(SAVE_DIR, filename)
    
    print("📸 Capturing screenshot in 2 seconds... Hold still!")
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot.save(full_path)
    print(f"✅ Screenshot saved as {full_path}")

def main():
    print("🟢 Press CTRL + SHIFT + / to capture your screen.")
    print("🔴 Press ESC to exit the program.")
    
    keyboard.add_hotkey('ctrl+shift+/', take_screenshot)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
