import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

API_TOKEN = "8313133136:AAEpQgcHfdFZHuVmDYMdyTs7n08CD_zaKN0"  # 👉 сюда вставь свой токен от @BotFather

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    # Главное меню с кнопками
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🗯️ Vridl Channel", url="https://t.me/vridlcompany")],
        [
            InlineKeyboardButton(text="🌐 Digital marketing", url="https://t.me/+SMAEqJlaZ5E3YzRi"),
            InlineKeyboardButton(text="🖌️ Design portfolio", url="https://t.me/+6ndGk_qcuXEwNTVi")
        ],
        [
            InlineKeyboardButton(text="⚕️ Creating Bots", url="https://t.me/+l4Q6lXe1V3EyMWJi"),
            InlineKeyboardButton(text="🆘 Support 24/7", url="https://t.me/evenokt")
        ],
        [
            InlineKeyboardButton(text="☯️ BOSS", url="https://t.me/evenokt"),
            InlineKeyboardButton(text="🗞️ Work", url="https://t.me/evenokt")
        ]
    ])

    # 🔹 Отправляем видео с приветственным текстом
    await message.answer_video(
        video="https://t.me/videobotjj/2",  # 👉 сюда вставь file_id или ссылку на .mp4
        caption=(
            "☯️ **VRIDL COMPANY** — это место бесконечной пустоты:\n\n"
            "🌐 Маркетинг, который работает\n"
            "🖌️ Дизайн, который цепляет\n"
            "⚕️ Боты, которые упрощают жизнь\n\n"
            "⚡ Рекламные чаты по городам —\n"
            "твоя площадка для продвижения в каждом регионе!\n\n"
            "Выбирай свой инструмент успеха 👇"
        ),
        parse_mode="Markdown"
    )

    # 🔹 Под видео выводим меню
    await message.answer("Меню:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

