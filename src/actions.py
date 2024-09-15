from const import State, Images
from main import logging
import pyautogui
from locate import safe_locate
import time
import traceback

def process_row(row, current_state):
    max_attempts = 5
    logging.info(f"Processing row: {row['card_number']}, {row['amount']}")
    
    try:
        logging.info("Clicking GIFT_CARD_SALE_BUTTON")
        click_button(Images.GIFT_CARD_SALE_BUTTON)
        time.sleep(1)
        
        logging.info(f"Entering card number: {row['card_number']}")
        pyautogui.write(row['card_number'])
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

def click_button(image_path, test_mode=True):
    location = safe_locate(image_path)
    if location:
        center = pyautogui.center(location)
        if test_mode:
            logging.info(f"Would click at {center} for image: {image_path}")
        else:
            pyautogui.click(center)
        return True
    logging.warning(f"Could not find image: {image_path}")
    return False
