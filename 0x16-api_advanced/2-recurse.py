#!/usr/bin/python3
"""get top ten titles for a subreddit from reddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
        }
    p = {'limit': 50, 'next_page': next_page, 'count': count}
    r = requests.get(url, allow_redirects=False,
                     headers=headers, params=p)
    if r.status_code != 200:
        return (None)
    rj = r.json().get('data')
    after = rj.get('after')
    children = rj.get('children')
    for child in children:
        title = child.get('data').get('title')
        hot_list.append(title)
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
