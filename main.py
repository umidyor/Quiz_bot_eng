import random
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
# # word_dict={}
keys=[]
values=[]
f=open("reading_dicts.txt","r")
f=f.read()
a=f.split("\n")
for i in a:
    if "-" in i:
        s=i.index("-")
        y1=i[:s]
        y2=i[s::]
        key=y1
        value=y2.strip("-")
        # Add the key-value pair to the dictionary
        # word_dict[key] = value
        keys.append(key)
        values.append(value)
        # dikt=dict(zip(key,value))
        # print(dikt)
#
#main
# num=random.randint(1,len(keys))
# key_rad=keys[num]
# val_rad=values[num]
# if values.index(val_rad)>len(values)/2:
#     other_rad1 = random.randint(1, len(keys))
#     val1_rad = values[other_rad1]
#     other_rad2 = random.randint(1, len(keys))
#     val2_rad = values[other_rad2]
# else:
#     other_rad1=random.randint(1,len(keys)/2)
#     val1_rad=values[values.index(val_rad)+other_rad1]
#     other_rad2=random.randint(1,len(keys)/2)
#     val2_rad=values[values.index(val_rad)+other_rad2]
#
# print(f"So'z:{key_rad}: \nA){val_rad}\nB){val1_rad}\nC){val2_rad}")

import random

def quesionare():
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

    options = [val_rad, val1_rad,val2_rad]
    random.shuffle(options)
    options_dict = {"A": options[0], "B": options[1], "C": options[2]}
    correct_answer = [key for key, value in options_dict.items() if value == val_rad][0]
#     print(f"So'z:{key_rad}:")
#     for option, value in options_dict.items():
#         print(f"{option}) {value}")
#
#     answer = input("Please enter your answer (A, B, or C): ")
#
#     if answer.upper() == correct_answer:
#         print("Correct! Your answer is right.")
#     else:
#         print(f"Sorry, your answer is incorrect. The correct answer is {correct_answer}.")
#
# # Ask the user to continue or quit
# while True:
quesionare()
#     another = input("Do you want to continue? (yes/no): ")
#     if another.lower() != 'yes':
#         break
#         print("Thanks for your participating")

# def questionnaire2():
#     num = random.randint(0, len(values) - 1)
#     val_rad = values[num]
#     key_rad = keys[num]
#
#     if keys.index(key_rad) > len(keys) / 2:
#         other_rad1 = random.randint(0, len(values) - 1)
#         key1_rad = keys[other_rad1]
#         other_rad2 = random.randint(0, len(values) - 1)
#         key2_rad = keys[other_rad2]
#     else:
#         other_rad1 = random.randint(0, len(values) // 2 - 1)
#         key1_rad = keys[(num + other_rad1) % len(keys)]
#         other_rad2 = random.randint(0, len(values) // 2 - 1)
#         key2_rad = keys[(num + other_rad2) % len(keys)]
#
#     options = [val_rad, key1_rad, key2_rad]
#     random.shuffle(options)
#     options_dict = {"A": options[0], "B": options[1], "C": options[2]}
#     correct_answer = [key for key, value in options_dict.items() if value == val_rad][0]
# questionnaire2()

from googletrans import Translator

# Create a Translator object
translator = Translator()

# Translate text from one language to another
result = translator.translate("Hello, how are you?", src="en", dest="uz")

# Access the translated text
translated_text = result.text

print(translated_text)

