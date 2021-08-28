from sys import path
path.append('..')
from SoroushBot import SoroushBot

bot_token = 'your bot token'

bot = SoroushBot(bot_token)

to = 'user chat_id'

[error, success] = bot.sendText(to, 'Your text')

if error:
    print('Sending message failed: {}' .format(error))
