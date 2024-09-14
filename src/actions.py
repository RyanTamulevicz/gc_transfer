from const import State
from main import logging
import pyautogui
from locate import safe_locate


def perform_action(state, test_mode=True):
    if state == State.MAIN_SCREEN:
        return click_button('gift_card_sale_button.png', test_mode=test_mode)
    elif state == State.GIFT_CARD_ENTRY:
        if test_mode:
            logging.info("Would type: TEMP")
        else:
            pyautogui.write('TEMP')
        return click_button('ok_button.png', test_mode=test_mode)
    elif state == State.AMOUNT_ENTRY:
        if test_mode:
            logging.info("Would type: 00.1")
        else:
            pyautogui.write('00.1')
        return click_button('ok_button.png', test_mode=test_mode)
    elif state == State.PAYMENT_SCREEN:
        return click_button('cash_button.png', test_mode=test_mode)
    else:
        logging.error(f"Unknown state: {state}")
        return False

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