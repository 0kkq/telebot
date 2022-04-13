from info import *
from rdod import *
from btns import * 
server = Flask(__name__)

logger = telebot.logger
logger.setLevel(logging.DEBUG)
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


@server.route(f"/{took}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://telemero.herokuapp.com/"+str(took))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) 
