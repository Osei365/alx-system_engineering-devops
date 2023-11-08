#!/usr/bin/python3
"""get top ten titles for a subreddit from reddit."""

import requests


def count_words(subreddit, word_list=[], after=None, words=None):
    if words is None:
        words = {}
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
                word = word.lower()
                words[word] = words.get(word, 0) + title.count(word)
    if after:
        return count_words(subreddit, word_list, after, words)
    sorted_dic = sorted(words.items(), key=lambda x: (-x[1], x[0]))
    for wd, freq in sorted_dic:
        print("{}: {}".format(wd, freq))
