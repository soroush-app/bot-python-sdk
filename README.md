
# Soroush Messenger Bot Python Library
Soroush Messenger Bot Wrapper for Python

## Dependencies ##
- Python 2.7+
- requests 
- sseclient-py

## Installation ##
Run the below commands
```bash
git clone https://github.com/soroush-app/bot-python-sdk
cd bot-python-sdk
pip install -r requirements.text
```

## Usage ##

```python
from client import Client

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


```
More examples are in the [examples](https://github.com/soroush-app/bot-python-sdk/tree/master/examples) folder.

 ## Contribute ##
 Contributions to the package are always welcome!
 - Report any idea, bugs or issues you find on the [issue tracker](https://github.com/soroush-app/bot-python-sdk/issues).
 - You can grab the source code at the package's [Git repository](https://github.com/soroush-app/bot-python-sdk.git).
