from env import ADMIN_ID, BOT_TOKEN
from telegram import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,BotCommand,ReplyKeyboardRemove
from telegram.ext import CommandHandler, Updater, CallbackQueryHandler,MessageHandler,Filters
import random
from datetime import datetime
from database import add_user_info,create_database
from in_key_buttons import lang,rating
from messages import message_handler
def help(update,context):
    update.message.reply_text(text="Change language:",reply_markup=InlineKeyboardMarkup(lang))
def top(update,context):
    pass
keys = []
values = []
f = open("reading_dicts.txt", "r")
f = f.read()
a = f.split("\n")
for i in a:
    if "-" in i:
        s = i.index("-")
        y1 = i[:s]
        y2 = i[s::]
        key = y1
        value = y2.strip("-")
        keys.append(key)
        values.append(value)

def start_command(update, context):
    update.message.reply_text("Please choose language😊:",reply_markup=InlineKeyboardMarkup(lang))
    context.bot.send_animation(chat_id=update.effective_chat.id,animation=open("sticker2.webp","rb"),reply_markup=ReplyKeyboardRemove())
    context.user_data['user_id']=update.message.from_user.id
    context.user_data['username']=update.message.from_user.username
    context.user_data['full_name']=update.message.from_user.full_name
    context.user_data.setdefault('trues', [])
    create_database()
    add_user_info(context.user_data['user_id'],context.user_data['username'],context.user_data['full_name'],len(context.user_data['trues']))

# def check_lang(update,context):
#     query=update.callback_query
#     if query.data=="eng":
#         context.bot.send_message(chat_id=query.message.chat_id,text=f"<b>Hi {context.user_data['full_name']} The mission of this bot is to help you increase your vocabulary⚡</b>", parse_mode="html")
#     elif query.data=="uzb":
#         context.bot.send_message(chat_id=query.message.chat_id,text=f"<b>Salom {context.user_data['full_name']} Ushbu botning vazifasi sizning so'z boyligingizni oshirishga yordam berishdir⚡</b>",parse_mode="html")
def quiz(update, context):
    num = random.randint(0, len(keys) - 1)
    key_rad = keys[num]
    val_rad = values[num]

    if values.index(val_rad) > len(values) / 2:
        other_rad1 = random.randint(0, len(keys) - 1)
        val1_rad = values[other_rad1]
        other_rad2 = random.randint(0, len(keys) - 1)
        val2_rad = values[other_rad2]
    else:
        other_rad1 = random.randint(0, len(keys) // 2 - 1)
        val1_rad = values[(num + other_rad1) % len(values)]
        other_rad2 = random.randint(0, len(keys) // 2 - 1)
        val2_rad = values[(num + other_rad2) % len(values)]

    options = [val_rad, val1_rad, val2_rad]
    random.shuffle(options)
    options_dict = {"A": options[0], "B": options[1], "C": options[2]}

    context.user_data['correct_answer'] = [key for key, value in options_dict.items() if value == val_rad][0]

    buttons = [
        [InlineKeyboardButton(f"A) {options_dict['A']}", callback_data='A')],
        [InlineKeyboardButton(f"B) {options_dict['B']}", callback_data='B')],
        [InlineKeyboardButton(f"C) {options_dict['C']}", callback_data='C')],
    ]

    text = f"What is the translation  of this word <strong>{key_rad}</strong>?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=InlineKeyboardMarkup(buttons),parse_mode="html")
continue_button=[[InlineKeyboardButton(text="Yes",callback_data="yes"),InlineKeyboardButton(text="No",callback_data="no")]]



def check_answer(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_answer = query.data
    correct_answer = context.user_data.get('correct_answer', '')

    if query.data == "eng":
        my_commands = [
            BotCommand("start", description="Restart the bot"),
            BotCommand('quiz', description="Start vocabulary test"),
            BotCommand("help", description="Change language"),
        ]
        context.bot.set_my_commands(my_commands)
        query.message.edit_text(
            text=f"<b>Hi {context.user_data['full_name']} The mission of this bot is to help you increase your vocabulary⚡Please click this /quiz command</b>",
            parse_mode="html"
        )
        context.bot.send_message(chat_id=chat_id,text="And you can see your and others level😁To do this, use the buttons below",reply_markup=rating)
    elif query.data == "uzb":
        query.message.edit_text(text=f"<b>Salom {context.user_data['full_name']} Ushbu botning vazifasi sizning so'z boyligingizni oshirishga yordam berishdir⚡Savol javob uchun ingliz tilini tanlang❗Agarda tarjimondan foydalanmoqchi bo'lsangiz, marhamat istagan tekstingizni yozing😊</b>", parse_mode="html")
    elif user_answer == "no":
        query.message.edit_text(text="Thanks for your participation😊")
        context.bot.send_video(chat_id=chat_id, video=open("ronaldo_go.gif", "rb"))
    elif user_answer == "yes":
        quiz(update, context)
    if user_answer == correct_answer:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query.message.edit_text(text=f"<strong>Correct!✅ Your answer is right ({timestamp}). Do you want to continue?</strong>", reply_markup=InlineKeyboardMarkup(continue_button), parse_mode="html")

    if query.data != "uzb" and query.data != "eng" and user_answer!="yes" and user_answer!="no" and user_answer != correct_answer:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query.message.edit_text(text=f"Hahaha😅 stupid! Your answer is incorrect. The correct answer is <strong>{correct_answer}</strong> ({timestamp}). Do you want to continue?", reply_markup=InlineKeyboardMarkup(continue_button), parse_mode="html")

    if user_answer == correct_answer:
        context.user_data['trues'].append(user_answer)

        result_trues = len(context.user_data['trues'])
        add_user_info(context.user_data['user_id'],context.user_data['username'], context.user_data['full_name'], result_trues)


def main():
    updater = Updater(token=BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("quiz", quiz))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(CallbackQueryHandler(check_answer))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
