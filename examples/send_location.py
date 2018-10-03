from sys import path
path.append('..')
from client import Client

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'

    [error, success] = bot.send_location(to, 35.7448416, 51.3753212)

    if success:
        print('Message sent successfully')
    else:
        print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
