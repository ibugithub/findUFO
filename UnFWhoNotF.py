import csv
import requests



username = "ibugithub"
token = "" 

def unFollowWhoNotF():
  with open('notFollowingMe.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      if row:
        user_to_unfollow = row[0]
        url = f"https://api.github.com/user/following/{user_to_unfollow}"
        response = requests.delete(url, auth=(username, token))
        
        if response.status_code == 204:
          print(f"Unfollowed {user_to_unfollow}")
        else:
          print(f"Failed to unfollow {user_to_unfollow}: {response.status_code} - {response.text}")
  

unFollowWhoNotF()