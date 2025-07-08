import requests

ytlink = input("Please Insert Youtuber Link:") #might add option @ to get youtuber

response = requests.get(ytlink)

#Checking if link is valid or not
if response.status_code == 404:
    print("Page not found (404)")
elif response.status_code == 200:
    print("Page loaded successfully!")