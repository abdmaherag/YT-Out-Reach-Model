import requests

ytlink = input("Please Insert Youtuber Link or @username:") #added option to lookup youtuber by @username

#look up youtuber by @username
if not ytlink.startswith ("http"):
    ytlink = f"https://www.youtube.com/@{ytlink}/videos"


#Checking if link is valid or not
try:
    response = requests.get(ytlink)

    if response.status_code == 404:
        print("Invalid Youtuber")
    elif response.status_code == 200:
        print("Valid Youtuber")

except requests.exceptions.MissingSchema:
    print("Invalid URL (Missing schema like https://).")
except requests.exceptions.RequestException as e:
    print(f" Network or URL error: {e}")


#STEP 2
