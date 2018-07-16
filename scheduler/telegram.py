import telepot

token = '389460165:AAEimDJ0HY3tJk9sd9HX1iHvjjUIG0hhAtM'
my_id = 240502830
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(240502830, text, parse_mode="Markdown")
