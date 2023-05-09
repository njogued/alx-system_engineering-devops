#!/usr/bin/python3
"""
Module to query the top 10 posts in a subreddit
"""

import requests


def top_ten(subreddit):
    """The top ten posts in a sub"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    custom_header = {"User-Agent": "My agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        hot_posts = response.json()

        for hot_post in hot_posts['data']['children']:
            print(hot_post['data']['title'])
    else:
        print(None)
