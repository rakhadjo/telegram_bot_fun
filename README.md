# Project <i>Telegram Bot Fun</i>
## (AKA Cursed Telegram Bot)
[![Build Status](https://travis-ci.com/rakhadjo/telegram_bot_fun.svg?branch=master)](https://travis-ci.com/rakhadjo/telegram_bot_fun)

Bot Name: cursed_bot <br>
Bot Username: @useless_joke_bot

## Supported commands
- `/start` starts the bot
- `/bop` returns a random dog image
- `/maw` returns a random cat image
- `/joke` returns a random joke
- `/kanyeQuote` returns a random Kanye West quote
- `/chucknorrisfax` returns a random fact about Chuck Norris
- more to come!

## Usage
Aside from the default Python gitignore, there is a `config.py` file that is in the `.gitignore`. `config.py` contains the API Key for the chat bot, and the random cat images API. 

The chat bot is hosted on heroku, under `cursed-telegram-bot`. 

FYI:
`config.py`:
```
key = 'chatbot_api_key'
cat_key = 'cat_images_api_key'
```

Run the `main.py` project, then the chat bot should activate, then run one of the supported commands provided above. 

## TODO: 
- Integrate with my [Cursed Images API](github.com/rakhadjo/cursed_images_api) after everything in that is done!
- Add the number guessing game
- Provide more commands to be supported (e.g. `/about`, `/github`)
- Maybe provide some conversation?

## REST APIs used:
- [Cat Images API](https://api.thecatapi.com/v1/images/search)
- [Dog Images API](https://random.dog/woof.json)
- [Random Jokes API](https://sv443.net/jokeapi/v2/joke/Any?format=json)
- [Kanye Rest API](https://api.kanye.rest)
- [Chuck Norris API](https://api.chucknorris.io/jokes/random)
