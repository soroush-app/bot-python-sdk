Soroush Messenger Bot Python SDK
================================

Soroush Messenger Bot Wrapper for Python |shiled| |travis| |badge|
|Documentation Status| |Updates|

Dependencies
------------

-  Python 2.7+
-  requests
-  sseclient-py

Installation
------------

.. code:: bash

   pip install soroush-python-sdk

Run the below commands

.. code:: bash

   git clone https://github.com/soroush-app/bot-python-sdk
   cd bot-python-sdk
   pip install -r requirements.txt

Usage
-----

.. code:: python

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

“to” value in above example is chat_id of a bot user. You can find it in
front of ‘from’ key in a message that user has sent to your bot. You can
see more examples in the `examples`_ directory.

## Contribute ## Contributions to the package are always welcome! -
Report any idea, bugs or issues you find on the `issue tracker`_. - You
can grab the source code at the package’s `Git repository`_.

.. _examples: https://github.com/soroush-app/bot-python-sdk/tree/master/examples
.. _issue tracker: https://github.com/soroush-app/bot-python-sdk/issues
.. _Git repository: https://github.com/soroush-app/bot-python-sdk.git

.. |shiled| image:: https://img.shields.io/pypi/v/soroush_python_sdk.svg
.. |travis| image:: https://img.shields.io/travis/alinik/soroush_python_sdk.svg
.. |badge| image:: https://readthedocs.org/projects/soroush-python-sdk/badge/?version=latest
.. |Documentation Status| image:: https://readthedocs.org/projects/bot-python-sdk/badge/?version=latest
   :target: https://bot-python-sdk.readthedocs.io/en/latest/?badge=latest
.. |Updates| image:: https://pyup.io/repos/github/alinik/bot-python-sdk/shield.svg
   :target: https://pyup.io/repos/github/alinik/bot-python-sdk/
