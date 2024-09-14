def determine_state():
    from locate import safe_locate
    from const import State, Images

    if safe_locate(Images.GIFT_CARD_SALE_BUTTON) and safe_locate(Images.ZERO_AMOUNT_STATE) and not safe_locate(Images.CARD_ID_STATE) and not safe_locate(Images.ENTER_AMOUNT):
        return State.MAIN_SCREEN
    elif safe_locate(Images.CARD_ID_STATE):
        return State.GIFT_CARD_ENTRY
    elif safe_locate(Images.ENTER_AMOUNT):
        return State.AMOUNT_ENTRY
    elif safe_locate(Images.GIFT_CARD_SALE_BUTTON) and safe_locate(Images.PAY_BUTTON) and not safe_locate(Images.ZERO_AMOUNT_STATE) and not safe_locate(Images.CARD_ID_STATE) and not safe_locate(Images.ENTER_AMOUNT):
        return State.PAYMENT_SCREEN
    elif safe_locate(Images.CHECKOUT_OPTIONS):
        return State.CHECKOUT
    else:
        return None