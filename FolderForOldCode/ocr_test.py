import pytesseract
import pyautogui
from PIL import Image
import time
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def take_screenshot(save_path="ocr_test_screenshot.png"):
    print("📸 Taking screenshot in 3 seconds... Move your mouse over the .txt file!")
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    print(f"✅ Screenshot saved to {save_path}")
    return save_path

def run_ocr(image_path):
    print("🔍 Running OCR...")
    text = pytesseract.image_to_string(Image.open(image_path))
    print("🧠 OCR Result:")
    print("--------------------------------------------------")
    print(text)
    print("--------------------------------------------------")
    return text

if __name__ == "__main__":
    path = take_screenshot()
    run_ocr(path)
