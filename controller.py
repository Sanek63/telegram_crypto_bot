import config
import sticker
from tg_rest import TgRest

from mode import Mode
from keyboard import Keyboard
from button_name import *

from aiogram import types

from utils import (
    enctypr_caesar,
    decrypt_caesar,
    qr_code
)

tg_rest = TgRest()


def request_to_tuple(
        text: str,
        sticker_id: str = None,
        keyboard: types.KeyboardButton = None,
):
    return text, sticker_id, keyboard


class Controller:

    def __init__(self, tg_id):
        # Текущий, предыдущий режимы
        self.now_mode = Mode.default
        self.last_mode = Mode.default

        self.tg_id = tg_id
        # Для запомминания ответов пользователя
        self.last_ans = None

    def change_mode(self, to_mode, last_ans=None):
        """
        Меняет режим приема команд
        :param last_ans: Последний ответ
        :param to_mode: Измененный мод
        """

        self.last_mode = self.now_mode
        self.now_mode = to_mode

        self.last_ans = last_ans

    def input(self, msg):
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """
        if self.now_mode == Mode.default:
            if msg == button_main_about:
                with open("about.txt", "r") as file:
                    data = file.read()

                return request_to_tuple(
                    data, keyboard=Keyboard.default_keyboard()
                )
            elif msg == button_main_cezar:
                self.change_mode(Mode.in_cezar)
                return request_to_tuple(
                    text="Вы выбрали шифр Цезаря. Какой метод шифрования хотите выбрать?",
                    keyboard=Keyboard.crypto_variables_keyboard()
                )
            elif msg == button_main_indechiffrable:
                self.change_mode(Mode.in_indechiffrable)
                return request_to_tuple(
                    text="Вы выбрали шифр Виженера. Какой метод шифрования хотите выбрать?",
                    keyboard=Keyboard.crypto_variables_keyboard()
                )
            elif msg == button_main_qr:
                self.change_mode(Mode.in_qr)
                return request_to_tuple(
                    text="Вы выбрали QR код. Для шифрование отправляйте любое сообщение",
                    keyboard=Keyboard.cancel_keyboard()
                )

            return request_to_tuple(
                text="Выберите вид шифрования", keyboard=Keyboard.default_keyboard()
            )

        if self.now_mode == Mode.in_qr:
            if msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            qr_path = qr_code(msg)
            tg_rest.send_photo(
                chat_id=self.tg_id,
                file_bytes=open(qr_path, "rb")
            )
            return request_to_tuple(
                text=f"Зашифрованное сообщение: {msg}", keyboard=Keyboard.cancel_keyboard()
            )

        if self.now_mode == Mode.in_cezar:
            if msg == button_encrypt:
                self.change_mode(Mode.cezar_encrypt)
                return request_to_tuple(
                    text="Напишите текст для шифрования", keyboard=Keyboard.cancel_keyboard()
                )
            elif msg == button_decrypt:
                self.change_mode(Mode.cezar_decrypt)
                return request_to_tuple(
                    text="Напишите текст для дешифрования", keyboard=Keyboard.cancel_keyboard()
                )
            elif msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            return request_to_tuple(
                text="Неизвестная команда", keyboard=Keyboard.crypto_variables_keyboard()
            )

        if self.now_mode == Mode.in_indechiffrable:
            if msg == button_encrypt:
                self.change_mode(Mode.indechiffrable_encrypt)
                return request_to_tuple(
                    text="Введите ключ, можно воспользоваться клавиатурой",
                    keyboard=Keyboard.numbers_keyboard()
                )
            elif msg == button_decrypt:
                self.change_mode(Mode.indechiffrable_decrypt)
                return request_to_tuple(
                    text="Введите ключ, можно воспользоваться клавиатурой",
                    keyboard=Keyboard.numbers_keyboard()
                )
            elif msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            return request_to_tuple(
                text="Неизвестная команда", keyboard=Keyboard.crypto_variables_keyboard()
            )

        if self.now_mode == Mode.cezar_encrypt:
            if msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )
            encrypted_text = enctypr_caesar(msg)
            return request_to_tuple(
                text=f"Зашифрованный текст = {encrypted_text}", keyboard=Keyboard.cancel_keyboard()
            )

        if self.now_mode == Mode.cezar_decrypt:
            if msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            decrypted_text = decrypt_caesar(msg)
            return request_to_tuple(
                text=f"Дешифрованный текст = {decrypted_text}", keyboard=Keyboard.cancel_keyboard()
            )

        if self.now_mode == Mode.indechiffrable_encrypt:
            if msg.isdigit():
                n = int(msg)
                if 1 <= n <= 33:
                    self.change_mode(Mode.in_indechiffrable_encrypt, n)
                    return request_to_tuple(
                        text="Напишите текст для дешифрования", keyboard=Keyboard.cancel_keyboard()
                    )

            elif msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            return request_to_tuple(
                text="Неверный ключ. Выберите повторно", keyboard=Keyboard.numbers_keyboard()
            )

        if self.now_mode == Mode.indechiffrable_decrypt:
            if msg.isdigit():
                n = int(msg)
                if 1 <= n <= 33:
                    self.change_mode(Mode.in_indechiffrable_decrypt, n)
                    return request_to_tuple(
                        text="Напишите текст для дешифрования", keyboard=Keyboard.cancel_keyboard()
                    )
            elif msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            return request_to_tuple(
                text="Неверный ключ. Выберите повторно", keyboard=Keyboard.numbers_keyboard()
            )

        if self.now_mode == Mode.in_indechiffrable_encrypt:
            if msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            encrypted_text = enctypr_caesar(msg, self.last_ans)
            return request_to_tuple(
                text=f"Зашифрованный текст = {encrypted_text}", keyboard=Keyboard.cancel_keyboard()
            )

        if self.now_mode == Mode.in_indechiffrable_decrypt:
            if msg == button_cancel:
                self.change_mode(Mode.default)
                return request_to_tuple(
                    text="Вы в главном меню", keyboard=Keyboard.default_keyboard()
                )

            decrypted_text = decrypt_caesar(msg, self.last_ans)
            return request_to_tuple(
                text=f"Дешифрованный текст = {decrypted_text}", keyboard=Keyboard.cancel_keyboard()
            )
