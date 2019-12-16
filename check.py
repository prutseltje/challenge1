#!/usr/bin/env python3
import requests
import time
import sys


url = 'http://10.10.0.5'


while True:
    try:
        r = requests.get(url, timeout=10)
        print('Get url {}: {}'.format(url, r.content.decode(r.encoding)))
        time.sleep(1)
    except requests.exceptions.RequestException:
        print('Time out, retry in 5 seconds')
        time.sleep(5)
    except KeyboardInterrupt:
        print('KeyboardInterrupt: Shutting down')
        sys.exit()
