from telegram.ext import Updater, CommandHandler
import requests
import re

from config import key

def get_url_dog(): 
	contents = requests.get('https://random.dog/woof.json').json()
	return contents['url']

def bop(bot, update):
	url = get_url_dog()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)

def get_url_cat():
    contents = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]
    print(contents)
    return contents

def maw(bot, update):
    url = get_url_cat()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('maw',maw))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()