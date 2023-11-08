#!/usr/bin/python3
"""get subsribers from reddit."""

import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
        }
    r = requests.get(url, allow_redirects=False, headers=headers)
    rj = r.json()
    if rj.get('error') == 404:
        return (0)
    return (rj.get('data').get('subscribers'))
