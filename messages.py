from functions import get_top_results,get_my_level,lang_trans
from googletrans import Translator
def message_handler(update,context):
    text=update.message.text
    if text=="Top 5🏆":
        get_top_results(update,context)
        context.bot.send_animation(chat_id=update.effective_chat.id, animation=open("sticker.webp", "rb"),
                                   caption="Very good results")
    if text=="My level🍁":
        get_my_level(update,context)
        context.bot.send_animation(chat_id=update.effective_chat.id,animation=open("mikey.webp","rb"),caption="Siuuuuuuuuuuuuuuuuuuuuuuuuu")
    if text!="My level🍁" and text!="Top 5🏆":
        lang_trans(update,context)


