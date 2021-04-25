from sys import path
path.append('..')
from SoroushBot import SoroushBot

bot_token = 'your bot token'
bot = SoroushBot(bot_token)

to = 'user chat_id'

[error, success] = bot.sendLocation(
                        target_id = to,
                        latitude =  35.7448416,
                        longitude = 51.3753212 ,
                        caption='Your Caption'
                   )

if error:
    print('error in sending video: {}' .format(error))

