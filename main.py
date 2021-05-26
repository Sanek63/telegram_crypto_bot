from aiogram import types
from aiogram.utils import executor

from session import bot, dp
from controller import Controller

users = {}


def get_controller(tg_id: int) -> Controller:
    if tg_id not in users:
        users[tg_id] = Controller(tg_id)

    return users[tg_id]


@dp.message_handler()
async def message(message: types.Message):
    tg_id = message.from_user.id

    controller = get_controller(tg_id)
    msg, sticker_id, keyboard = controller.input(message.text)

    if sticker_id:
        await message.answer_sticker(sticker_id)

    await bot.send_message(
        chat_id=tg_id,
        text=msg,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

if __name__ == '__main__':
    executor.start_polling(dp)