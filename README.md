# telecambot
Getting images from webcam by telegram bot in python3.

#### Dependencies:

```apt install python3-pip python3-dev python3-opencv build-essential libssl-dev libffi-dev libgnutls28-dev```

#### Running

Update 'Get rid of proxy, because it works unstable'.

  
To run the program use ./main.py

The bot sends logs to an error.log file.  

There are two user types in the bot. It's required to controll access to the bot. 
 
The botext.py contains the list_admin = ['username'] and list_user = []. 

Admin has the following rights:

the list of commands: 

1) /cmd add username  - Add user to an access list

2) /cmd rm username - remove user from an access list

3) /cmd list - show an access list

4) /cmd status - show interfaces, cpu temperature, uptime. 


Should work <i>infinitely</i>. Otherwise - open an issue.

Do not forget to set your <i>bot token</i>.
