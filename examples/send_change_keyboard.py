from sys import path
path.append('..')
from client import Client

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'

    keyboard1 = [
            [{'command': "1.1", 'text': "button 1"}, {'command': "1.2", 'text': "button 2"}],
            [{'command': "2.1", 'text': "button 3"}, {'command': "2.2", 'text': "button 4"}, {'command': "2.3", 'text': "button 5"}],
    ]
    keyboard2 = bot.make_keyboard('Back')
    keyboard3 = bot.make_keyboard('Button1|Button2|Button3')
    keyboard4 = bot.make_keyboard('Button1|Button2|Button3\nButton4\nButton5|Button6')
    keyboard5 = bot.make_keyboard([['Row1Button1', 'Row1Button2'], ['Row2Button1']])
    keyboard6 = bot.make_keyboard([[['Row1Button1', 'help'], ['Row1Button2', 'back']], [['Row2Button1', 'options']]])
    keyboard7 = bot.make_keyboard([[{'text': 'Row1Button1'}, {'text': 'Row1Button2'}], [{'text': 'Row2Button1'}]])
    keyboard8 = bot.make_keyboard(
        [[{'text': 'Row1Button1', 'command': 'help'}, {'text': 'Row1Button2', 'command': 'back'}],
         [{'text': 'Row2Button1', 'command': 'options'}]])

    [error, success] = bot.change_keyboard(to, keyboard4)

    if success:
        print('Keyboard changed successfully')
    else:
        print('Error in changing keyboard: {}' .format(error))

except Exception as e:
    print(e.args[0])
