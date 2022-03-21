import argparse
import clive.clive
import sys

def run():
    """Given a feed name will start a listening socket and print new posts
       as they arrive. The name is the last part of the live feed URL:

        https://www.reddit.com/live/wmk50bsm9vt3

       in this case: wmk50bsm9vt3"""
    parser = argparse.ArgumentParser(description='''Follow Reddit live feeds
            from the comfort of your terminal''')
    parser.add_argument('--width', '-w', dest='text_width', default=70,
            help='Set the maximum textwidth of feed. Default 70')

    args, remain = parser.parse_known_args()

    if len(remain) < 1:
        print('You need to provide the name of the feed. Eg: wmk50bsm9vt3')
        sys.exit(0)

    feed = remain[0]

    cli = clive.clive.Clive(feed, args.text_width)
    cli.run()
