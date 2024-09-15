from pynput import mouse
from pynput.mouse import Button, Controller
from const import State, Images
from main import logging
import pyautogui
from locate import safe_locate
import time
import traceback

# Initialize the mouse controller
mouse = Controller()

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
        pyautogui.write(str(row['amount']))
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
            logging.info(f"Moving mouse to {center}")
            mouse.position = (center.x, center.y)
            time.sleep(0.5)
            logging.info(f"Clicking at {mouse.position}")
            mouse.click(Button.left)
            logging.info(f"Clicked at {center}")
        except Exception as e:
            logging.error(f"Failed to click: {e}")
        return True
    logging.warning(f"Could not find image: {image_path}")
    return False

def test_mouse_control():
    try:
        logging.info("Starting mouse control test")
        
        # Get the current mouse position
        current_pos = mouse.position
        logging.info(f"Current mouse position: {current_pos}")
        
        # Move the mouse to a specific position
        test_x, test_y = 100, 100
        logging.info(f"Attempting to move mouse to ({test_x}, {test_y})")
        mouse.position = (test_x, test_y)
        time.sleep(1)
        
        # Get the new position
        new_pos = mouse.position
        logging.info(f"New mouse position: {new_pos}")
        
        # Check if the mouse moved
        if new_pos == (test_x, test_y):
            logging.info("Mouse movement successful")
        else:
            logging.warning("Mouse did not move to the expected position")
        
        # Move mouse back to original position
        mouse.position = current_pos
        logging.info("Moved mouse back to original position")
        
        # Test click
        logging.info("Testing click (moving to (200, 200) and clicking)")
        mouse.position = (200, 200)
        time.sleep(1)
        mouse.click(Button.left)
        logging.info("Click test completed")
        
    except Exception as e:
        logging.error(f"Error in mouse control test: {str(e)}")
        logging.error("Traceback:", exc_info=True)