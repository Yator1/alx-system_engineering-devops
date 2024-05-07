#!/usr/bin/python3
"""
A module that Querries Reddit API and returns the total number of subscribers for a
given subreddit.
If an invalid subreddit is given, return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Querries the API and returns total subscribers for a given subreddit,
       or 0 if invalid subreddit given.
    """
    headers = {"User-Agent": "TitoRedditBot"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0
    else:             
        return 0