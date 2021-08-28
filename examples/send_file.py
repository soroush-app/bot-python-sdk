from sys import path
path.append('..')
from SoroushBot import SoroushBot

bot_token = 'your bot token'
bot = SoroushBot(bot_token)

to = 'user chat_id'
path = 'your file path'

[error, success] = bot.sendFile(
                        target_id = to,
                        file_path = path,
                        caption='Your Caption'
                   )

if error:
    print('error in sending file: {}' .format(error))
