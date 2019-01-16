#!/usr/bin/python3
import time 
import os
import psutil

def stop():
    for script in ['webcam.py','botext.py']:
        if script in (p.name() for p in psutil.process_iter()):
            pid_bot = next(item for item in psutil.process_iter() if item.name() == script).pid
            os.system('kill -9 {0}'.format(pid_bot))
            print('stoped ', script)
        else:
            pass 

def run():

    stop()

    os.system('./{0} &'.format('botext.py'))
    print('Started botext.py')

    os.system('./{0} &'.format('webcam.py'))
    print('Started webcam.py')


def main():
    run()
    while 'botext.py' in (p.name() for p in psutil.process_iter()):
        time.sleep(30)
    stop() 

if __name__ == '__main__':
    main()
