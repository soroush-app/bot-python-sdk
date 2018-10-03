from sys import path
path.append('..')
from client import Client

bot_token = 'your bot token'
bot = Client(bot_token)

try:
    file_url = 'received file url from server'
    save_file_path = 'path to save the file'

    [error, downloaded_file_path] = bot.download_file(file_url, save_file_path)

    if downloaded_file_path:
        print('file downloaded successfully in {}' .format(downloaded_file_path))
    else:
        print('error in downloading file: {}' .format(error))

except Exception as e:
    print(e.args[0])