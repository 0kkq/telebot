from info import * 
from insert import * 

def reply(m):
	if 'hi' in m.text:
		bot.reply_to(m, 'نجب')
	elif m.text=='السلام عليكم':
		bot.reply_to(m, 'وعليكم السلام خاللي 🌚💞')
		
		
		#kick
	elif m.text=='طرد':
		ban = bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
		if ban :
			bot.send_message(m.chat.id, 'سلملي 🌚💞' + '  \n @' + m.reply_to_message.from_user.username)
	elif m.text=='/ban':
		ban = bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
		if ban :
			bot.send_message(m.chat.id, 'سلملي 🌚💞' + '  \n @' + m.reply_to_message.from_user.username)
	elif m.text=='ابلع':
		ban = bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
		if ban :
			bot.send_message(m.chat.id, 'سلملي 🌚💞' + '  \n @' + m.reply_to_message.from_user.username)

#ch-commands
	elif 'زخرفه'in m.text:
		en_zkh(m)
	elif 'اضف رد' in m.text:
		insert(m)
	elif 'حذف'in m.text:
		delete(m)
	elif 'ايدي'in m.text:
		info_tele(m)
	else:
		replayx(m)