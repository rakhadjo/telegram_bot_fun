from telegram.ext import Updater, CommandHandler
import requests
import re
import os
PORT = int(os.environ.get('PORT', 5000))

from config import key, cat_key
# key = '1153261086:AAGbv-YS9a8jQPfsz2bPK0h-9HHUPpdL72k'
# cat_key = '9fd87723-e4ae-4213-a09f-45162b17753c'

def get_url_dog(): 
	contents = requests.get('https://random.dog/woof.json').json()
	return contents['url']

def bop(bot, update):
	url = get_url_dog()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)

def get_url_cat():
    header = {'x-api-key': cat_key}
    contents = requests.get('https://api.thecatapi.com/v1/images/search', headers=header).json()[0]
    return contents['url']

def maw(bot, update):
    url = get_url_cat()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def joke(bot, update):
    contents = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=json').json()
    chat_id = update.message.chat_id
    update.message.reply_text(contents['setup'] + '\n\n' + contents['delivery'])

def kanyeQuote(bot, update):
    contents = requests.get('https://api.kanye.rest').json()
    chat_id = update.message.chat_id
    update.message.reply_text('"' + contents['quote'] + '"')

def chuckNorrisFax(bot, update):
    contents = requests.get('https://api.chucknorris.io/jokes/random').json()
    chat_id = update.message.chat_id
    update.message.reply_text('Chuck Norris Fact ' + contents['id'] + ':\n\n' + contents['value'])


def main():
	# Create Updater Instance
	# Passing the Bot API Key
    updater = Updater(key)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Different Commands
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('maw',maw))
    dp.add_handler(CommandHandler('joke',joke))
    dp.add_handler(CommandHandler('kanyeQuote',kanyeQuote))
    dp.add_handler(CommandHandler('chuckNorrisFax',chuckNorrisFax))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", 
    	port=int(PORT),
    	url_path=key)
    updater.bot.setWebhook('https://cursed-telegram-bot.herokuapp.com/' + key)


    # Run the bot, until interrupted in the terminal
    updater.idle()
    
if __name__ == '__main__':
    main()