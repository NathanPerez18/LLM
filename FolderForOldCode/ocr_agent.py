import os
import time
import pytesseract
import pyautogui
import keyboard
from datetime import datetime
from PIL import Image

# 🛠️ Set Tesseract path (Windows only — adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
    return full_path

def run_ocr(image_path):
    print("🔍 Running OCR...")
    text = pytesseract.image_to_string(Image.open(image_path))
    print("🧠 OCR Result:")
    print("--------------------------------------------------")
    print(text.strip())
    print("--------------------------------------------------")
    return text

def capture_and_analyze():
    image_path = take_screenshot()
    extracted_text = run_ocr(image_path)
    # 👉 Later: send image + text to GPT-4 Vision here
    return extracted_text

def main():
    print("🟢 Press CTRL + SHIFT + / to scan your screen for text.")
    print("🔴 Press ESC to exit.")
    
    keyboard.add_hotkey('ctrl+shift+/', capture_and_analyze)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
