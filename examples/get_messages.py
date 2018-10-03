from sys import path
path.append('..')
from client import Client

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    messages = bot.get_messages()
    for message in messages:
        print("New message from {} \nType: {}\nBody: {}" .format(message['from'], message['type'], message['body']))

except Exception as e:
    print(e.args[0])