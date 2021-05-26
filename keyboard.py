from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from button_name import *


class Keyboard:
    @staticmethod
    def default_keyboard():
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)

        button_1 = KeyboardButton(button_main_qr)
        button_2 = KeyboardButton(button_main_indechiffrable)
        button_3 = KeyboardButton(button_main_cezar)
        button_4 = KeyboardButton(button_main_about)

        greet_kb.row(button_1, button_2, button_3)
        greet_kb.row(button_4)

        return greet_kb

    @staticmethod
    def crypto_variables_keyboard():
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)

        button_1 = KeyboardButton(button_encrypt)
        button_2 = KeyboardButton(button_decrypt)
        button_3 = KeyboardButton(button_cancel)

        greet_kb.row(button_1, button_2)
        greet_kb.row(button_3)

        return greet_kb

    @staticmethod
    def cancel_keyboard():
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(button_cancel)
        greet_kb.row(button_1)

        return greet_kb

    @staticmethod
    def numbers_keyboard():
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1_1 = KeyboardButton("1")
        button_1_2 = KeyboardButton("2")
        button_1_3 = KeyboardButton("3")
        button_1_4 = KeyboardButton("4")
        button_2_1 = KeyboardButton("5")
        button_2_2 = KeyboardButton("6")
        button_2_3 = KeyboardButton("7")
        button_2_4 = KeyboardButton("8")
        button_3_1 = KeyboardButton("9")
        button_3_2 = KeyboardButton("10")
        button_3_3 = KeyboardButton("11")
        button_3_4 = KeyboardButton("12")
        button_4_1 = KeyboardButton("13")
        button_4_2 = KeyboardButton("14")
        button_4_3 = KeyboardButton("15")
        button_4_4 = KeyboardButton("16")
        button_5_1 = KeyboardButton("17")
        button_5_2 = KeyboardButton("18")
        button_5_3 = KeyboardButton("19")
        button_5_4 = KeyboardButton("20")
        button_6_1 = KeyboardButton("21")
        button_6_2 = KeyboardButton("22")
        button_6_3 = KeyboardButton("23")
        button_6_4 = KeyboardButton("24")
        button_7_1 = KeyboardButton("25")
        button_7_2 = KeyboardButton("26")
        button_7_3 = KeyboardButton("27")
        button_7_4 = KeyboardButton("28")
        button_8_1 = KeyboardButton("29")
        button_8_2 = KeyboardButton("30")
        button_8_3 = KeyboardButton("31")
        button_8_4 = KeyboardButton("32")
        button_8_5 = KeyboardButton("33")
        button_9 = KeyboardButton("Отмена")

        greet_kb.row(button_1_1, button_1_2, button_1_3, button_1_4)
        greet_kb.row(button_2_1, button_2_2, button_2_3, button_2_4)
        greet_kb.row(button_3_1, button_3_2, button_3_3, button_3_4)
        greet_kb.row(button_4_1, button_4_2, button_4_3, button_4_4)
        greet_kb.row(button_5_1, button_5_2, button_5_3, button_5_4)
        greet_kb.row(button_6_1, button_6_2, button_6_3, button_6_4)
        greet_kb.row(button_7_1, button_7_2, button_7_3, button_7_4)
        greet_kb.row(button_8_1, button_8_2, button_8_3, button_8_4, button_8_5)
        greet_kb.row(button_9)

        return greet_kb
