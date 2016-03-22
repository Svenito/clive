#!/bin/env python2.7

import signal
import requests
import sys
import json
import colorama
import textwrap
import websocket
import datetime
from HTMLParser import HTMLParser
unescape = HTMLParser().unescape

user_agent = 'CLI:clive by /u/tame_robot'
quitting = False

def signal_handler(signal, frame):
    global quitting
    quitting = True
    sys.exit(0)


def print_item(item):
    body = item['body']
    body.replace('\t', '\n')
    body = textwrap.wrap(body)
    formatted_body = '\n'.join(body)

    timestamp = item['created_utc']
    posted_at = datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')

    print ('%s%s%s\n%s' %
          (colorama.Style.BRIGHT, posted_at, colorama.Style.RESET_ALL,
           formatted_body))
    print ('%s%s ...................................%s' %
            (colorama.Fore.YELLOW, colorama.Style.BRIGHT,
            colorama.Style.RESET_ALL))


def on_message(socket, msg):
    msg = json.loads(msg)
    if msg['type'] == 'update':
        data = msg['payload']['data']
        if data['stricken']:
            return
        print_item(data)


def on_close(socket):
    """Socket expired, fetch a new one"""
    if not quitting:
        init_socket(feed)


def init_socket(feed):
    w_socket = get_socket(feed)
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(w_socket, on_message=on_message,
                                on_close=on_close)
    ws.run_forever()


def get_socket(feed_name):
    headers = {'User-Agent': user_agent}
    r = requests.get('http://www.reddit.com/live/%s/about.json' % feed_name, headers=headers)
    data = r.json()
    return unescape(data['data']['websocket_url'])


if __name__ == '__main__':
    global feed

    test = 'wmk50bsm9vt3'
    feed = test

    signal.signal(signal.SIGINT, signal_handler)
    init_socket(feed)
