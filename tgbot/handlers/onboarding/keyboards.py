from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text


def make_keyboard_for_start_command(is_approved) -> InlineKeyboardMarkup:
    buttons = []
    buttons.append(InlineKeyboardButton(help_button_text, callback_data=f'{CBD_help_button}'))
    if is_approved:
        buttons.append(InlineKeyboardButton(change_time_button_text, callback_data=f'{CBD_change_time_button}'))
    buttons_list = [
        buttons
        
    ]

    return InlineKeyboardMarkup(buttons_list)
