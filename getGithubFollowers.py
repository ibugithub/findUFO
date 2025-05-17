import requests
import csv

followers = []
followings = []

matchedPair = []
notFollowingMe = []

def get_github_followers(username, token=None):
    
    url = f"https://api.github.com/users/{username}/followers"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            raise Exception(f"GitHub API error: {response.status_code} - {response.text}")
        
        data = response.json()
        if not data:
            break
        followers.extend(data)
        page += 1
    return [f['login'] for f in followers]


def get_github_followings(username, token=None):
    
    url = f"https://api.github.com/users/{username}/following"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            raise Exception(f"GitHub API error: {response.status_code} - {response.text}")
        
        data = response.json()
        if not data:
            break
        followings.extend(data)
        page += 1
    return [f['login'] for f in followers]


def analyze():
    for following in followings:
        if following in followers:
            matched = {}
            matched['following'] = following['login']
            matched['follower'] = following['login']
            matchedPair.append(matched)
        else:
            notFollowingMe.append(following['login'])

def convert_to_csv():
    with open('matched.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['following', 'follower'])
        writer.writeheader()
        writer.writerows(matchedPair)
        
    with open('notFollowingMe.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['notFollowingMe'])
        for user in notFollowingMe:
            writer.writerow([user])
    

your_username = "ibugithub"
your_token = "u" 


get_github_followers(your_username, your_token)
get_github_followings(your_username, your_token)
analyze()
convert_to_csv()

print('the followers are:', len(followers))
print('the following are:', len(followings))
