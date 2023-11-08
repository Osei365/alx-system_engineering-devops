#!/usr/bin/python3
"""get top ten titles for a subreddit from reddit."""

import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
        }
    p = {'limit': 10}
    r = requests.get(url, allow_redirects=False,
                     headers=headers, params=p)
    rj = r.json()
    if rj.get('error') == 404:
        print(None)
        return
    children = rj.get('data').get('children')
    [print(child.get('data').get('title')) for child in children]
