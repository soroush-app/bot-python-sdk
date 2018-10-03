from sys import path
path.append('..')
from client import Client
from os.path import getsize
import ntpath

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'
    video_path = 'your video path'
    video_thumbnail_path = 'video thumbnail path'
    video_duration_in_milliseconds = 7000

    [video_error, video_url] = bot.upload_file(video_path)
    if video_error:
        print('error in uploading video: {}' .format(video_url))
    else:
        print('video uploaded successfully with url: {}' .format(video_url))

    if video_url:
        [thumbnail_error, thumbnail_url] = bot.upload_file(video_thumbnail_path)
        if thumbnail_error:
            print('error in uploading thumbnail: {}' .format(thumbnail_error))
        else:
            print('thumbnail uploaded successfully with url: {}' .format(thumbnail_url))

        [error, success] = bot.send_video(to, video_url, ntpath.basename(video_path), getsize(video_path),
                                          video_duration_in_milliseconds, 512, 512,
                                          thumbnail_url,
                                          caption='your caption')

        if success:
            print('Message sent successfully')
        else:
            print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
