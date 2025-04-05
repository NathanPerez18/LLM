import os
import time
import pytesseract
import pyautogui
import keyboard
from datetime import datetime
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI

# Load .env and OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Tesseract config (adjust if needed on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Directory to save screenshots
SAVE_DIR = "captured_screens"

def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def take_screenshot():
    ensure_save_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    full_path = os.path.join(SAVE_DIR, filename)

    print(" Capturing screenshot in 2 seconds...")
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot.save(full_path)
    print(f" Screenshot saved as {full_path}")
    return full_path

def run_ocr(image_path):
    print(" Running OCR...")
    text = pytesseract.image_to_string(Image.open(image_path))
    print(" OCR Result:")
    print("--------------------------------------------------")
    print(text.strip())
    print("--------------------------------------------------")
    return text

def analyze_text_with_gpt(user_text):
    print(" Sending to GPT for scam analysis...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Does the following message look like a scam or phishing attempt? Be specific in your reasoning.\n\nMessage: {user_text}"
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def capture_analyze_display():
    image_path = take_screenshot()
    extracted_text = run_ocr(image_path)

    if extracted_text.strip():
        analysis = analyze_text_with_gpt(extracted_text)
        print("\n GPT Scam Analysis:")
        print("--------------------------------------------------")
        print(analysis)
        print("--------------------------------------------------")
    else:
        print("⚠️ No text was detected in the screenshot. Try again with a clearer image.")

def main():
    print("🟢 Scam Sniffer is running!")
    print("📸 Press CTRL + SHIFT + / to scan your screen.")
    print("🔴 Press ESC to exit.")

    keyboard.add_hotkey('ctrl+shift+/', capture_analyze_display)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
