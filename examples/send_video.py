from sys import path
path.append('..')
from SoroushBot import SoroushBot

bot_token = 'your bot token'
bot = SoroushBot(bot_token)

to = 'user chat_id'
path_video = 'your video path'
path_video_thumbnail = 'your thumbnail of video path'

[error, success] = bot.sendVideo(
                        target_id = to,
                        video_path = path_video,
                        video_thumbnail_path = path_video_thumbnail ,
                        caption='Your Caption'
                   )

if error:
    print('error in sending video: {}' .format(error))
