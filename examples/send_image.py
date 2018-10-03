from sys import path
path.append('..')
from client import Client
from os.path import getsize
import ntpath

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'
    image_path = 'image path'
    image_thumbnail_path = 'thumbnail path'

    [image_error, image_url] = bot.upload_file(image_path)
    if image_error:
        print('error in uploading image: {}' .format(image_error))
    else:
        print('image uploaded successfully with url: {}' .format(image_url))

    if image_url:
        [thumbnail_error, thumbnail_url] = bot.upload_file(image_thumbnail_path)
        if thumbnail_error:
            print('error in uploading thumbnail: {}' .format(thumbnail_error))
        else:
            print('thumbnail uploaded successfully with url: {}' .format(thumbnail_url))

        [error, success] = bot.send_image(to, image_url, ntpath.basename(image_path), getsize(image_path), 512, 512,
                                          thumbnail_url,
                                          caption='your caption')

        if success:
            print('Message sent successfully')
        else:
            print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
