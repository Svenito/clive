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


class Clive(object):
    def __init__(self, feed_name):
        self.feed_name = feed_name
        self.user_agent = 'CLI:clive by /u/tame_robot'
        self.quitting = False
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signal, frame):
        """Handle CTRL+C to stop reconnection"""
        self.quitting = True
        sys.exit(0)

    def print_item(self, item):
        """Print a new item to the terminal formatted to 70chars width"""
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

    def on_message(self, socket, msg):
        """Receive a new message, parse it, format it and print it"""
        msg = json.loads(msg)
        if msg['type'] == 'update':
            data = msg['payload']['data']
            if data['stricken']:
                return
            self.print_item(data)

    def on_close(self, socket):
        """Socket expired, fetch a new one if we're not quitting
        Unfortunately the websockets expire after a while"""
        if not self.quitting:
            self.init_socket()

    def run(self, debug=False):
        """Get the websocket URL and connect to it and start the process"""
        print 'Connecting to live feed... ',
        socket_url = self.socket_url()

        websocket.enableTrace(debug)
        ws = websocket.WebSocketApp(socket_url, on_message=self.on_message,
                                    on_close=self.on_close)
        print 'Connected.\n'
        ws.run_forever()

    def socket_url(self):
        """Retrieve the websocket url from the feed name"""
        headers = {'User-Agent': self.user_agent}
        r = requests.get('http://www.reddit.com/live/%s/about.json' %
                         self.feed_name, headers=headers)
        data = r.json()
        return unescape(data['data']['websocket_url'])


if __name__ == '__main__':
    """Given a feed name will start a listening socket and print new posts
    as they arrive. The name is the last part of the live feed URL:
        https://www.reddit.com/live/wmk50bsm9vt3

    in this case: wmk50bsm9vt3"""

    if len(sys.argv) < 2:
        print 'You need to provide the name of the feed. Eg: wmk50bsm9vt3'
        sys.exit(0)

    feed = sys.argv[1]= 'wmk50bsm9vt3'
    clive = Clive(feed)
    clive.run()

