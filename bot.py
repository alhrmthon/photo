import os
import pyrogram
import requests
import asyncio
from pyrogram import Client, filters as ay
from time import sleep
import telebot

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
token = os.environ.get("TOKEN")

app = Client("bot", bot_token=token, api_id = api_id, api_hash = api_hash)

@app.message_handler(commands=['start'])
async def start(client, message):
    if message.chat.type == 'private':
   	 first = message.from_user.first_name
   	 photo = 'https://telegra.ph/file/5df7ac7c2fcf0166a82fc.jpg'
   	 a = types.InlineKeyboardMarkup(row_width=1)
   	 b = types.InlineKeyboardButton(text='ℹ️ developer', url='t.me/VR_LA')
   	 h = types.InlineKeyboardButton(text='✅ change language', callback_data='lang')
   	 a.add(h,b)
   	 bot.send_photo(message.chat.id , photo=photo , caption=f'<strong>Hi {first} ðŸ‘‹\n- - - - - - - - -\n Welcome to the old picture coloring bot\n please send me a link of photo\n on telegraph or from @top4top_bot\nBy: @VR_LA</strong>',parse_mode='html',reply_markup=a)
    
@app.message_handler(func=lambda m:True)
def photo(client, message):
	msg = message.text
	bot.send_message(message.chat.id, text=f"please wait",parse_mode="html")
	r = requests.post(
    "https://api.deepai.org/api/colorizer",
    data={
        'image': f'{msg}',
    },
    headers={'api-key': '6ad07515-ccf3-48e7-a4c6-eafaa2aa04b6'}
).json()
	m = r['output_url']
	a = types.InlineKeyboardMarkup(row_width=1)
	b = types.InlineKeyboardButton(text='么𝗩𝗜𝗥𝗨𝗦™ ',url='t.me/VR_LA')
	a.add(b)
	bot.send_photo(message.chat.id,m, caption=f"""<strong>
By : @VR_LA
</strong>""" ,parse_mode='html',reply_to_message_id=message.message_id,reply_markup=a)
pass

@app.callback_query_handler(func=lambda call:True)
def callback(client, call):
	if call.message:
		if call.data == 'lang':
			name =call.from_user.first_name
			a = types.InlineKeyboardMarkup(row_width=1)
			b = types.InlineKeyboardButton(text='ℹ️ مبرمج البوت', url='t.me/VR_LA')
			h = types.InlineKeyboardButton(text='✅ تغيير اللغه', callback_data='lang1')
			a.add(h,b)
			bot.edit_message_caption(chat_id=call.message.chat.id ,message_id=call.message.message_id , caption="مرحبا {} \n☣️\nمرحبا بك في بوت تلوين الصور \nارسل لي رابط الصورة \nتليجراف او @top4top_bot\nBy : @VR_LA".format(name),reply_markup=a)
		if call.data == 'lang1':
		 	 a = types.InlineKeyboardMarkup(row_width=1)
		 	 b = types.InlineKeyboardButton(text='ℹ️ developer', url='t.me/VR_LA')
		 	 h = types.InlineKeyboardButton(text='✅ change language', callback_data='lang')
		 	 a.add(h,b)
		 	 first = call.from_user.first_name
		 	 bot.edit_message_caption(chat_id=call.message.chat.id , message_id=call.message.message_id , caption='<strong>Hi {} ðŸ‘‹\n- - - - - - - - -\n Welcome to the old picture coloring bot\n please send me a link of photo\n on telegraph or from @top4top_bot\nBy: @VR_LA</strong>'.format(first),parse_mode='html',reply_markup=a)
			
			
bot.infinity_polling(True)