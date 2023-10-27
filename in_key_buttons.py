from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
lang=[
    [InlineKeyboardButton("Eng🇬🇧",callback_data="eng"), InlineKeyboardButton("Uzb🇺🇿",callback_data="uzb")]
]

rating=[
    [KeyboardButton("My level🍁"),KeyboardButton("Top 5🏆")]
]
rating=ReplyKeyboardMarkup(rating,resize_keyboard=True,one_time_keyboard=True)

