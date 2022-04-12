from info import *
from rdod import *
from btns import * 
#server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
	idd = m.from_user.id
	if Admin==idd:
		bot.send_message(m.chat.id, 'WELLCOME BRO :/', parse_mode='html', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'zkh':
        en_zkh(call.message)
@bot.message_handler(func = lambda m : True)
def rdod(m):
	reply(m)


bot.infinity_polling()
