#!/usr/bin/env python3
""" Twitter Downloader
"""
import argparse
import logging
import lxml.etree

import twitter_scraper

LOGGER = logging.getLogger('twit-dl')

DEFAULT_SAVE_PATH_FORMAT = './{twitter_user.lower}/{filename}'

ARGP = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
ARGP.add_argument('twitter_users', nargs='+')
ARGP.add_argument(
    '--save-path-format',
    default=DEFAULT_SAVE_PATH_FORMAT,
    help=(
        'Safe path format\n'
        'DEFAULT: {}'
    ).format(DEFAULT_SAVE_PATH_FORMAT)
)
ARGP.add_argument('--dump-links', action='store_true')

def _safety_scrape(generator):
    while True:
        try:
            yield next(generator)
        except lxml.etree.ParserError as err:
            LOGGER.error(err)


def main(argp=None):
    if argp is None:
        argp = ARGP.parse_args()

    logging.basicConfig()

    for twitter_user in argp.twitter_users:
        print(twitter_user)

        for tweet in _safety_scrape(twitter_scraper.get_tweets(
                user=twitter_user,
                pages=100,
        )):
            for photo in tweet['entries']['photos']:
                if argp.dump_links:
                    print(photo)
                    continue
                raise NotImplementedError
            # import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
