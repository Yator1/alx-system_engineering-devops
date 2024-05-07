
#!/usr/bin/python3
"""
A module that querries the Reddit API and returns a list of the titles of all hot posts
listed for a given subreddit
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of the titles of all hot posts listed for a subreddit"""
    headers = {"User-Agent": "TitoRedditBot"}
    params = {"after": after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = json.loads(response.text).get('data').get('children')
    after = json.loads(response.text).get('data').get('after')
    if data is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for item in data:
            hot_list.append(item.get('data').get('title'))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
