#!/usr/bin/python3
"""get top ten titles for a subreddit from reddit."""

import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
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
    next_page = rj.get('next_page')
    count += rj.get('dist')
    children = rj.get('children')
    [hot_list.append(child.get('data').get('title')) for child in children]
    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)
    return hot_list
