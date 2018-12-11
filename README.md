# telecambot
Getting images from webcam by telegram bot in python3.


If you need <i>proxy</i> - just uncomment line in botext.py and set valid proxy url.

Dependencies:

apt install python3-pip python3-dev python3-opencv build-essential libssl-dev libffi-dev libgnutls28-dev

pip3 install setuptools psutil proxybroker python-telegram-bot PySocks

To run the program use ./proxy.py

The proxy.py script contains a configuration of proxy servers. It searches free proxy servers from the global list.

The bot sends logs to an error.log file. If there is a HTTPError it interrupts process and starts job with a new proxy server. 

There are two user types in the bot. It requires for the controlling an access to the bot. 
 
The botext.py contains the list_admin = ['username'] and list_user = []. 

Admin has the following rights:

the list of commands: 

1) /user add username  - Add user to an access list

2) /user rm username - remove user from an access list

3) /user list - show an access list


Should works <i>infinitely</i>. Otherwise - open an issue.

Do not forget to set your <i>bot token</i>.
