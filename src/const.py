from enum import Enum
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class State:
    MAIN_SCREEN = "MAIN_SCREEN"
    GIFT_CARD_ENTRY = "GIFT_CARD_ENTRY"
    AMOUNT_ENTRY = "AMOUNT_ENTRY"
    PAYMENT_SCREEN = "PAYMENT_SCREEN"
    CHECKOUT = "CHECKOUT"
    COMPLETED = "COMPLETED"

class Images(Enum):
    GIFT_CARD_SALE_BUTTON = resource_path('images/button_images/gift_card_sale_button.png')
    ZERO_AMOUNT_STATE = resource_path('images/button_images/zero_amount_state.png')
    CARD_ID_STATE = resource_path('images/button_images/card_id_state.png')
    ENTER_AMOUNT = resource_path('images/button_images/enter_amount.png')
    PAY_BUTTON = resource_path('images/button_images/pay_button.png')
    CHECKOUT_OPTIONS = resource_path('images/button_images/checkout_options.png')

# class Images(Enum):
#     GIFT_CARD_SALE_BUTTON = 'src/images/button_images/gift_card_sale_button.png'
#     ZERO_AMOUNT_STATE = 'src/images/button_images/zero_amount_state.png'
#     CARD_ID_STATE = 'src/images/button_images/card_id_state.png'
#     ENTER_AMOUNT = 'src/images/button_images/enter_amount.png'
#     # GIFT_CARD_ENTRY = 'src/images/button_images/gift_card_entry.png'
#     # AMOUNT_ENTRY = 'src/images/button_images/amount_entry.png'
#     PAY_BUTTON = 'src/images/button_images/pay_button.png'
#     CHECKOUT_OPTIONS = 'src/images/button_images/checkout_options.png'
#     # OK_BUTTON = 'src/images/button_images/ok_button.png'
#     # CASH_BUTTON = 'src/images/button_images/cash_button.png'

# required_images = [
#     'src/images/button_images/gift_card_sale_button.png',
#     'src/images/button_images/zero_amount_state.png',
#     'src/images/button_images/card_id_state.png',
#     # 'src/images/button_images/gift_card_entry.png',
#     # 'src/images/button_images/amount_entry.png',
#     # 'src/images/button_images/pay_button.png',
#     # 'src/images/button_images/ok_button.png',
#     # 'src/images/button_images/cash_button.png'
# ]