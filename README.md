
# Soroush Messenger Bot Python SDK
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
pip install -r requirements.txt
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
"to" value in above example is chat_id of a bot user. You can find it in front of 'from' key in a message that user has sent to your bot. 
You can see more examples in the [examples](https://github.com/soroush-app/bot-python-sdk/tree/master/examples) directory.

 ## Contribute ##
 Contributions to the package are always welcome!
 - Report any idea, bugs or issues you find on the [issue tracker](https://github.com/soroush-app/bot-python-sdk/issues).
 - You can grab the source code at the package's [Git repository](https://github.com/soroush-app/bot-python-sdk.git).
