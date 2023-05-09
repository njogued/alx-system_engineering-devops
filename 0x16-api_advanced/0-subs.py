#!/usr/bin/python3
'''
A script to return the number of subscribers on a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    """Function to calc the number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    agent_header = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=agent_header, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        subscribers = json_data.get("data").get("subscribers")
        return subscribers
    else:
        return 0
