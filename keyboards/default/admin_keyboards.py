from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xabar Yuborish ๐ ')
        ],
        [
            KeyboardButton(text='Kanal โ'),
            KeyboardButton(text='Kanal โ')
        ],
        [
            KeyboardButton(text="Kanallar ๐"),
            KeyboardButton(text="Statistika ๐")
        ],
        [
            KeyboardButton(text="Rasmni almashtirish ๐ผ "),
            KeyboardButton(text="Sovg'alar ro'yxatini kiritish๐"),
        ],
        [
            KeyboardButton(text="Taklif miqdorini kiritish ๐"),
            KeyboardButton(text="O'yin haqida matn ๐ฎ")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xabar Yuborish ๐ ')
        ],
        [
            KeyboardButton(text='Kanal โ'),
            KeyboardButton(text='Kanal โ')
        ],
        [
            KeyboardButton(text="Kanallar ๐"),
            KeyboardButton(text="Statistika ๐")
        ],
        [
            KeyboardButton(text="๐ Bosh menu")

        ]
    ],
    resize_keyboard=True
)
