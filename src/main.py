from pynput import mouse
from pynput.mouse import Button, Controller
import logging
import os
from state import determine_state
from const import Images, State
import time
from data import Data
import pygetwindow
import traceback
import pyautogui

log_dir = 'log'
mouse = Controller()

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f'log_{time.strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


def check_image_files():
    missing_files = []
    for image in Images:
        full_path = os.path.abspath(image.value)
        logging.info(f"Checking image file: {full_path}")
        if not os.path.exists(full_path):
            missing_files.append(full_path)
        else:
            logging.info(f"Found image file: {full_path}")
    
    if missing_files:
        logging.error(f"Missing image files: {', '.join(missing_files)}")
        return False
    return True

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

def main(test_mode=True):
    from actions import process_row
    test_mouse_control()
    logging.info(f"Current working directory: {os.getcwd()}")
    
    if not check_image_files():
        logging.error("Exiting due to missing image files.")
        return

    max_attempts = 5
    data = Data()
    logging.info(f"Data loaded: {data.data.shape[0]} rows")
    cash_register_window = pygetwindow.getWindowsWithTitle('Register')[0] 
    print(f"Total rows to process: {data.data.shape[0]}")

    row_index = 0
    total_rows = data.data.shape[0]

    while row_index < total_rows:
        input("Press Enter to process the next 20 rows...")
        
        rows_to_process = min(20, total_rows - row_index)
        
        for i in range(rows_to_process):
            current_row = data.data.iloc[row_index]
            logging.info(f"Processing row: {row_index} {current_row['card_number']}, {current_row['amount']}")
            cash_register_window.activate() 
            time.sleep(2)
            process_row(current_row)
            
            row_index += 1
        
        print(f"Processed {rows_to_process} rows. Total progress: {row_index}/{total_rows}")

    print("All rows have been processed.")

    
    # while current_state != State.COMPLETED and max_attempts > 0:
    #     logging.info(f"Current state: {current_state}")
        
    #     if current_state is None:
    #         logging.warning("Could not determine current state")
    #         max_attempts -= 1
    #         time.sleep(1)
    #         current_state = determine_state()
    #         continue
        
    #     if perform_action(current_state, test_mode):
    #         time.sleep(1)
    #         current_state = determine_state()
    #     else:
    #         logging.error(f"Failed to perform action for state: {current_state}")
    #         max_attempts -= 1
        
    # if current_state == State.COMPLETED:
    #     logging.info("Process completed successfully")
    # else:
    #     logging.error("Process failed to complete")

if __name__ == "__main__":
    try:
        main(test_mode=True)  # Set to False for actual execution
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        logging.error("Traceback details:\n" + traceback.format_exc())
        input("Press Enter to continue...")