#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return "OK"

    data = response.json().get('data', {}).get('children', [])
    for post in data:
        print(post['data']['title'])

    # ✅ Always return "OK" at the end
    return "OK"
