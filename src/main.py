import logging
import os
from state import determine_state
from const import Images
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define states

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

def main(test_mode=True):
    logging.info(f"Current working directory: {os.getcwd()}")
    
    if not check_image_files():
        logging.error("Exiting due to missing image files.")
        return

    max_attempts = 5
    while True:
        current_state = None
        time.sleep(2)
        current_state = determine_state()
        print(f"State: {current_state}")
    
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
        input("Press Enter to continue...")