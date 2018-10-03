from sys import path
path.append('..')
from client import Client

bot_token = 'your bot token'
bot = Client(bot_token)

try:
    messages = bot.get_messages()
    for message in messages:
        print("New message from {} \nType: {}\nBody: {}".format(message['from'], message['type'], message['body']))
        message['to'] = message['from']
        message.pop('from')
        message.pop('time')

        [error, success] = bot.send_message(message)

        if success:
            print('Message sent successfully')
        else:
            print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
