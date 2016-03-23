#!/usr/bin/env python

import signal
import requests
import sys
import json
import colorama
import textwrap
import websocket
import datetime
try:
    from HTMLParser import HTMLParser
    unescape = HTMLParser().unescape
except ImportError:
    from html import unescape


class Clive(object):
    def __init__(self, feed_name):
        self.feed_name = feed_name
        self.user_agent = 'CLI:clive by /u/tame_robot'
        self.quitting = False
        self.reconnecting = False
        signal.signal(signal.SIGINT, self.signal_handler)

        self.title = ''
        self.description = ''
        self.state = ''

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

    def on_error(self, socket, error):
        print ('Socket error: ', error)
        self.quitting = True
        sys.exit(0)

    def on_close(self, socket):
        """Socket expired, fetch a new one if we're not quitting
        Unfortunately the websockets expire after a while"""
        if not self.quitting:
            self.reconnecting = True
            self.run()

    def on_open(self, socket):
        """Print connected message. Does not print if
        reconnecting from expired socket"""
        if not self.reconnecting:
            print ('Connected. Press Ctrl+c twice to quit.\n')
            print (colorama.Style.BRIGHT + self.title)
            print (self.description + colorama.Style.RESET_ALL)
            print ('Feed status is: %s' % self.state)

    def run(self, debug=False):
        """Get the websocket URL and connect to it and start the process"""
        print ('Connecting to live feed... ')
        socket_url = self.socket_url()

        websocket.enableTrace(debug)
        ws = websocket.WebSocketApp(socket_url,
                                    on_message=self.on_message,
                                    on_close=self.on_close,
                                    on_error=self.on_error,
                                    on_open=self.on_open)
        ws.run_forever()

    def socket_url(self):
        """Retrieve the websocket url from the feed name"""
        headers = {'User-Agent': self.user_agent}
        r = requests.get('http://www.reddit.com/live/%s/about.json' %
                         self.feed_name, headers=headers)

        error = False
        if r.status_code != 200:
            error = True

        try:
            about = r.json()
        except ValueError:
            error = True

        if error:
            print ('Failed to get websocket address for feed')
            sys.exit(1)

        data = about['data']
        self.title = data['title']
        self.description = data['description']
        self.state = data['state']
        return unescape(data['websocket_url'])
