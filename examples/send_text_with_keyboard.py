from sys import path

path.append('..')
from client import Client

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'

    # creating keyboard yourself
    keyboard1 = [
        [{'command': "1.1", 'text': "button 1"}, {'command': "1.2", 'text': "button 2"}],
        [{'command': "2.1", 'text': "button 3"}, {'command': "2.2", 'text': "button 4"}, {'command': "2.3", 'text': "button 5"}],
    ]

    # just one button
    keyboard2 = bot.make_keyboard('Back')

    # a row with 3 buttons
    keyboard3 = bot.make_keyboard('Button1|Button2|Button3')

    # 3 rows
    keyboard4 = bot.make_keyboard('Button1|Button2|Button3\nButton4\nButton5|Button6')

    # 2 rows, each row is a list of button texts
    keyboard5 = bot.make_keyboard([['Row1Button1', 'Row1Button2'], ['Row2Button1']])

    # 2 rows, each row is a list of button lists, each button is a list of [text, command]
    keyboard6 = bot.make_keyboard([[['Row1Button1', 'help'], ['Row1Button2', 'back']], [['Row2Button1', 'options']]])

    # 2 rows. each row is a list of button dictionaries, each button is a dictionary os {'text':'your text'}
    keyboard7 = bot.make_keyboard([[{'text': 'Row1Button1'}, {'text': 'Row1Button2'}], [{'text': 'Row2Button1'}]])

    # 2 rows. each row is a list of button dictionaries, each button is a dictionary os {'text': 'your text', 'command: 'your command'}
    keyboard8 = bot.make_keyboard(
        [[{'text': 'Row1Button1', 'command': 'help'}, {'text': 'Row1Button2', 'command': 'back'}],
         [{'text': 'Row2Button1', 'command': 'options'}]])

    [error, success] = bot.send_text(to, 'Your text', keyboard=keyboard6)

    if success:
        print('Message sent successfully')
    else:
        print('Sending message failed: {}'.format(error))

except Exception as e:
    print(e.args[0])
