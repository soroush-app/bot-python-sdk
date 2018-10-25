from soroush_python_sdk import Client


bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'

    [error, success] = bot.send_text(to, 'Your text')

    if success:
        print('Message sent successfully')
    else:
        print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
