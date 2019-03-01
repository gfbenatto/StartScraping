import urllib.request
import json

"""
Searching for news about Python notices on Reddit.
"""

url = 'https://www.reddit.com/r/Python/.json'
resp = urllib.request.urlopen(url).read()

parsed = json.loads(resp.decode('utf-8'))

for item in parsed['data']['children']:
    doc = item['data']
    print(doc['title'])
    print(doc['url'])
    print()
