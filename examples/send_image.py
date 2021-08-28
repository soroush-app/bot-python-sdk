from sys import path
path.append('..')
from SoroushBot import SoroushBot

bot_token = 'your bot token'
bot = SoroushBot(bot_token)

to = 'user chat_id'
path_image = 'image path'
path_image_thumbnail = 'thumbnail path'

[error, success] = bot.sendImage(
                        target_id = to,
                        image_path = path_image,
                        image_thumbnail_path = path_image_thumbnail ,
                        caption='Your Caption'
                   )

if error:
    print('error in sending image: {}' .format(error))
