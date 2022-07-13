import requests
from time import sleep
import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"<strong>Hi {first} 👋\n- - - - - - - - -\n Welcome to the old picture coloring bot\nBy: @VR_LA</strong>",parse_mode="html")
@bot.message_handler(func=lambda m: True)
def start(message):
	msg = message.text
	bot.send_message(message.chat.id, text=f"please wait",parse_mode="html")
	r = requests.post(
    "https://api.deepai.org/api/colorizer",
    data={
        'image': f'{msg}',
    },
    headers={'api-key': '6ad07515-ccf3-48e7-a4c6-eafaa2aa04b6'}
).json()
	m = r["output_url"]
	bot.send_photo(message.chat.id,m, caption=f"""<strong>
By : @VR_LA
</strong>""" ,parse_mode='html',reply_to_message_id=message.message_id)
pass
bot.polling(True)