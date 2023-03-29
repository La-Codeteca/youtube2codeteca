import requests

def get_videos(channel_id:str, TOKEN:str):
    url = f"https://www.googleapis.com/youtube/v3/search?key={TOKEN}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20"
    try: 
        r = requests.get(url)
        return r
    except requests.exceptions.HTTPError as err:
        print(f"ERROR [{r.status_code}] : {r.text}")
        raise SystemExit(err)
    

def get_channel_id(channel_name:str):
    url = f"https://www.googleapis.com/youtube/v3/channels?key={TOKEN}&forUsername=trastejant"
    try: 
        r = requests.get(url)
        return r
    except requests.exceptions.HTTPError as err:
        print(f"ERROR [{r.status_code}] : {r.text}")
        raise SystemExit(err)