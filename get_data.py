import json
import requests as r
import os

USER = ('etra0', 'pass')

def download_data():
    data = r.get('https://api.github.com/user/repos', auth=USER)
    with open("data.json", "w") as f:
        f.write(data.text)

download_data()
os.system("mkdir data;mkdir img")
with open('data.json') as f:
    text = f.read()

text = json.loads(text)
for repo in text:
    with open('data/' + repo['name'], 'w') as f:
        print(repo['name'])
        f.write(r.get(repo['url'] + '/commits', auth=USER).text)
