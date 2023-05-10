#!/usr/bin/python3
"""
Retrieve titles for posts
a recursive function to return list containing the titles of all hot articles
"""

import requests as re


def recurse(subreddit, hot_list=[], after=None):
    """If not a valid subreddit, return None"""
    custom_header = {"User-agent": "My agent"}
    s = subreddit
    a = after
    u = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(s, a)
    hotposts = re.get(u, headers=custom_header, allow_redirects=False)

    if hotposts.status_code == 200:
        post_info = hotposts.json()['data']
        after = posts['after']
        posts = post_info["children"]
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
