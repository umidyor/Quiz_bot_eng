import sqlite3
from googletrans import Translator


def get_top_results(update, context):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username, full_name, results FROM user_info ORDER BY results DESC LIMIT 5")

    results = cursor.fetchall()

    conn.close()

    if not results:
        update.message.reply_text(text="<b>Unfortunately, no one has run the test yet and has not shown any results😔Maybe you will be the first, click /quiz and test yourself🥹</b>", parse_mode="html")
    else:
        message = "\n".join([
            f"<b>{i + 1} </b><strong><a href='https://t.me/{user[0]}'>{user[1]}</a>'s result is {user[2]}</strong>"
            for i, user in enumerate(results)
        ])
        update.message.reply_text(message, parse_mode="html")


def get_my_level(update,context):
    conn=sqlite3.connect("data.db")
    c=conn.cursor()
    c.execute(f"WITH SortedUsers AS (SELECT username, full_name, user_id, results,ROW_NUMBER() OVER (ORDER BY results DESC) AS position FROM user_info) SELECT position, username, full_name, results FROM SortedUsers WHERE user_id = {update.message.from_user.id}")

    results=c.fetchone()
    conn.close()
    if results is None:
        update.message.reply_text("<b>But you haven't done the quiz yet. That's why you don't have any points. Please click the /quiz command first and collect points by starting the quiz😉</b>",parse_mode="html")
    else:
        l=[i for i in results]
        update.message.reply_text(
            f"Your level are <b>{l[0]}</b>🏆Dear {l[2]} your total score <strong>{l[3]}</strong> .Never stop🚫",parse_mode="html"
        )
def detect_language(text):
    translator = Translator()
    detected = translator.detect(text)
    return detected.lang

def lang_trans(update,context):

    if detect_language(update.message.text)=='en':
        translator = Translator()
        text=update.message.text
    # Translate text from one language to another
        result = translator.translate(f"{text}", src="en", dest="uz")

    # Access the translated text
        translated_text = result.text
        update.message.reply_text(text=translated_text)
    if detect_language(update.message.text)=='uz':
        translator = Translator()
        text = update.message.text
        # Translate text from one language to another
        result = translator.translate(f"{text}", src="uz", dest="en")

        # Access the translated text
        translated_text = result.text
        update.message.reply_text(text=translated_text)


