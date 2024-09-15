from const import State, Images
from main import logging
import pyautogui
from locate import safe_locate
import time
import traceback


pyautogui.PAUSE = 1  # Add a pause between pyautogui commands
pyautogui.FAILSAFE = True  # Enable fail-safe

def process_row(row):
    max_attempts = 5
    
    try:
        logging.info("Clicking GIFT_CARD_SALE_BUTTON")
        click_button(Images.GIFT_CARD_SALE_BUTTON)
        time.sleep(1)
        
        logging.info(f"Entering card number: {row['card_number']}")
        pyautogui.write(str(row['card_number']))
        time.sleep(0.5)
        
        logging.info("Clicking OK_BUTTON")
        click_button(Images.OK_BUTTON)
        time.sleep(1)
        
        logging.info(f"Entering amount: {row['amount']}")
        pyautogui.write(row['amount'])
        time.sleep(0.5)
        
        logging.info("Pressing 'enter'")
        pyautogui.press('enter')
        time.sleep(1)
        
    except Exception as e:
        logging.error(f"Error processing row: {row['card_number']}, {row['amount']}")
        logging.error("Traceback details:\n" + traceback.format_exc())
        raise e

def click_button(image_path, test_mode=False):
    location = safe_locate(image_path)
    if location:
        center = pyautogui.center(location)
        try:
            pyautogui.moveTo(center.x, center.y)
            time.sleep(0.5)
            pyautogui.click()
            logging.info(f"Clicked at {center}")
        except Exception as e:
            logging.error(f"Failed to click: {e}")
        return True
    logging.warning(f"Could not find image: {image_path}")
    return False
