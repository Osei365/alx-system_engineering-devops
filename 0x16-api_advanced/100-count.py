#!/usr/bin/python3
"""get top ten titles for a subreddit from reddit."""

import requests


def count_words(subreddit, word_list=[], after=None, words=None):
    if words is None:
        words = []
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
        subreddit, after)
    headers = {
        'User-Agent': 'Mozilla/5.0'
        }
    r = requests.get(url, allow_redirects=False,
                     headers=headers)
    if r.status_code != 200:
        return (None)
    rj = r.json().get('data')
    after = rj.get('after')
    children = rj.get('children')
    for child in children:
        title = child.get('data').get('title')
        title = title.lower()
        for word in word_list:
            if word.lower() in title:
                words.append(word.lower())
    if after:
        return count_words(subreddit, word_list, after, words)
    dic = {}
    for wd in words:
        if wd in dic.keys():
            dic[wd] += 1
        else:
            dic[wd] = 1
    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for wd, freq in sorted_dic:
        print("{}: {}".format(wd, freq))
