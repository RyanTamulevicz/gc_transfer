
from main import logging
import os
import pyautogui
from datetime import datetime

def safe_locate(image_path):
    full_path = os.path.abspath(image_path.value)
    logging.info(f"Attempting to locate image: {full_path}")
    try:
        return pyautogui.locateOnScreen(full_path, confidence=0.7)
    except pyautogui.ImageNotFoundException:
        logging.warning(f"Image not found on screen: {full_path}")
        return None
    except Exception as e:
        logging.error(f"Error locating image {full_path}: {str(e)}")
        # screenshot_path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        # pyautogui.screenshot(screenshot_path)
        # logging.info(f"Screenshot saved to {screenshot_path}")
        return None