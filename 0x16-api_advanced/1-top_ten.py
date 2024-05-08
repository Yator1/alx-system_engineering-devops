#!/usr/bin/python3
"""
This module contains querries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    headers = {"User-Agent": "TitoRedditBot"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("None")
        return
    data = json.loads(response.text).get('data').get('children')
    if not data:
        print("None")
        return
    for item in data[0:10]:
        print(item.get('data').get('title'))
