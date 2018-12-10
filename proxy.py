#!/usr/bin/python3

import asyncio
import time
import os
import psutil
from proxybroker import Broker

def proxygen():

    async def show(proxies):
        while True:
            proxy = await proxies.get()
            if proxy is None: break
            print('Found proxy: {0}:{1}\nlocation: {2}\nconnection: {3} '.format(proxy.host, proxy.port, proxy.geo[1], proxy.avg_resp_time))
            return (proxy.host, proxy.port)

    proxies = asyncio.Queue()
    broker = Broker(proxies)
#, verify_ssl=True, max_tries=1, timeout=1)
    tasks = asyncio.gather(
        broker.find(types=['SOCKS5'], countries = ['US', 'DE', 'FR', 'BE', 'CN', 'NL', 'UA', 'BY', 'IT'], limit=1),
        show(proxies))

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(tasks)[1]

def stop():

    for script in ['webcam.py','botext.py']:

        if script in (p.name() for p in psutil.process_iter()):

            pid_bot = next(item for item in psutil.process_iter() if item.name() == script).pid
            os.system('kill -9 {0}'.format(pid_bot))
            print('stoped ', script)

        else:
            pass

def run(proxy):

    stop()

    for script in ['webcam.py','botext.py']:

        if script == 'botext.py':
            os.system('./{0} {1} {2} &'.format(script, proxy[0], proxy[1]))
            print('Started ', script)
        else:
            os.system('./{0} &'.format(script))
            print('Started ', script)

def read(name):

    with open(name) as f:
        lineList  = f.readlines()
        f.close()
    return lineList

def main():

    run(proxygen())

    lines = len(read('error.log'))

    while 'botext.py' in (p.name() for p in psutil.process_iter()):

        new_lines = read('error.log')

        if lines < len(new_lines):

            lines = len(new_lines)

            if 'HTTPError' in new_lines[-1]:
                run(proxygen())
            else:
                print(new_lines[-1])
                time.sleep(2)
        else:

            time.sleep(5)
    stop()

if __name__ == '__main__':

    main()
