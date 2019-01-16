#!/usr/bin/python3
import logging
import sys
import psutil
import datetime

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,
							TimedOut, ChatMigrated, NetworkError)

#proxy = sys.argv[1]
#port = sys.argv[2]

auth = True
list_admin = ['']
list_user = ['']


TOKEN = ''
REQUEST_KWARGS = {
#     'proxy_url': 'socks5://{0}:{1}'.format(proxy,port)
# Optional, if you need authentication:
# 'urllib3_proxy_kwargs': {
#     'username': 'PROXY_USER',
#     'password': 'PROXY_PASS',
# }
}


def run_bot():

	updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
	dispatcher = updater.dispatcher

	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='error.log', level=logging.ERROR)

	def error_callback(bot, update, error):
		try:
			raise error
		except BadRequest:
			print('BadRequest',error)
			logging.error(error)
		# handle malformed requests - read more below!
		except TimedOut:
			print('TimedOut', error)
			logging.error(error)
		# handle slow connection problems
		except NetworkError:
			print('NetworkError', error)
			logging.error(error)
		# handle other connection problems

	dispatcher.add_error_handler(error_callback)

	def authentication(username,level):
		if level == 'user':
			if username in list_user or username in list_admin:
				return True

		elif level == 'admin':
			if username in list_admin:
				return True


	def cmd(bot, update):

		if authentication(str(update.message.from_user.username),'admin') == True:
			command = str(update.message.text).split(None)

		if command[1] == 'add' and len(command) == 3:
		
			if command[2] not in list_user:
				list_user.append(command[2])
				bot.send_message(chat_id=update.message.chat_id, text="user {0} has been added".format(command[2]))

		elif command[1] == 'rm' and len(command) == 3:
			
			if command[2] in list_user:
				list_user.remove(command[2])
				bot.send_message(chat_id=update.message.chat_id, text="user {0} has been removed".format(command[2]))

		elif command[1] =='list':
			bot.send_message(chat_id=update.message.chat_id, text="{0}".format(list_user))

		elif command[1] =='status':

			info = {}
			list_int={}

			for i in psutil.net_if_addrs():
				list_int[i] = psutil.net_if_addrs()[i][0][1]

			info['interface'] = list_int
			info['temp'] = psutil.sensors_temperatures()['iio_hwmon'][0][1] 
			info['uptime'] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

			bot.send_message(chat_id=update.message.chat_id, text="{0}".format(info))

	if auth == True:
		user_handler = CommandHandler('cmd', cmd)
		dispatcher.add_handler(user_handler)
	else:
		pass

	def start(bot, update):
		bot.send_message(chat_id=update.message.chat_id, text="I'm a super bot, i know /webcam command!")

	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)

	def echo(bot, update):
		bot.send_message(chat_id=update.message.chat_id,
		text="use commands with slash(/) please")  # update.message.text)

	echo_handler = MessageHandler(Filters.text, echo)
	dispatcher.add_handler(echo_handler)

	def webcam(bot, update):
		if auth == True:
			if authentication(str(update.message.from_user.username),'user') == True:
				bot.send_photo(chat_id=update.message.chat_id, photo=open('img.png', 'rb'))
			else:
				bot.send_message(chat_id=update.message.chat_id, text="Sorry, you are not authorized person. Please, contact with @{0}".format(list_admin[0]))
		else:
			bot.send_photo(chat_id=update.message.chat_id, photo=open('img.png', 'rb'))

	webcam_handler = CommandHandler('webcam', webcam)
	dispatcher.add_handler(webcam_handler)


	def unknown(bot, update):
		bot.send_message(chat_id=update.message.chat_id, text="sorry, I understand only /webcam command.")

	unknown_handler = MessageHandler(Filters.command, unknown)
	dispatcher.add_handler(unknown_handler)

	updater.start_polling()
	updater.idle()
	updater.stop()
	print("telegram bot done")


if __name__ == "__main__":
	run_bot()
