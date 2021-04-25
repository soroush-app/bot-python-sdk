
# Soroush Messenger Bot Python SDK

Use SoroushBot.py to send video ,image and file easier ! 

if you can ,please help us to complete this script (SoroushBot.py) .

## Installation ##
Run the below commands
```bash
git clone https://github.com/soroush-app/bot-python-sdk
cd bot-python-sdk
pip install -r requirements.txt
```

## Usage ##

```python
from SoroushBot import SoroushBot

bot_token = 'your bot token'

bot = SoroushBot(bot_token)

to = 'user chat_id'

[error, success] = bot.sendText(to, 'Your text')

if success:
    print('Message sent successfully')



```
"to" value in above example is chat_id of a bot user. You can find it in front of 'from' key in a message that user has sent to your bot. 
You can see more examples in the [examples](https://github.com/soroush-app/bot-python-sdk/tree/master/examples) directory.

use [SoroushBot](https://github.com/Mahdiali313/bot-python-sdk/blob/master/SoroushBot.py) function becuase it's easier to use!

 ## Contribute ##
 Contributions to the package are always welcome!
 - Report any idea, bugs or issues you find on the [issue tracker](https://github.com/soroush-app/bot-python-sdk/issues).
