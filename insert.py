from info import *

#اضافه رد

def insert(m):
	Tmsg = m.text
	Tmsg = Tmsg.split()[2: ]
	Tmsg = ' '.join(map(str, Tmsg))
	replaysfile = open('replays.txt', 'a', encoding='utf-8')
	replaysfile.write('\n')
	replaysfile.write(Tmsg)
	replaysfile.close()




    
    
    
#الرد ع الرد المضاف
def replayx(m):
		with open('replays.txt', 'r', encoding='utf-8') as tx:
			for i in tx.readlines():
				word = i.split(':')[0]
				if word==m.text:
					reply_words = i.split(':')[1]
					bot.reply_to(m, reply_words)


#zkhrafa engilsh for test


def en_zkh(m):
	url='https://dev-apisfree.pantheonsite.io/ZA/ZA.php?text='
	zkhtxt = m.text
	zkhtxt = zkhtxt.split()[1: ]
	zkhtxt = ' '.join(map(str, zkhtxt))
	d=requests.get(url+zkhtxt)
	api_zkh=d.json()
	zkh_2g=api_zkh['newTEXT']
	msg_zkh = ' تمت الزخرفه ياعمري 🌚💞 '+'\n\n\n'+zkh_2g
	bot.reply_to(m, msg_zkh)
	
	#INFO 
	
def info_tele(m):
		idd = str(m.from_user.id)
		user = m.from_user.username
		name = m.from_user.first_name+m.from_user.last_name
		idmsg = f'''\n __________\n 𝐧𝐚𝐦𝐞 : {name}\n 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @{user}\n 𝐢𝐝 : {idd} 
		
		\n
		'''
		bot.reply_to(m, idmsg)


