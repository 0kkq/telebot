import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from info import *
from flask import Flask, request

server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


bot.delete_webhook()

@bot.message_handler(commands=['start'])
def startt(m):
	bot.reply_to(m, 'hi')
	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	   			if call.data == 'zkh':
	   				en_zkh(call.message)
@bot.message_handler(func = lambda m : True)
def rdod(m):
	reply(m)

		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://telemero.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.infinity_polling()
