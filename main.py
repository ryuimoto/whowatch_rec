import requests
from bs4 import BeautifulSoup

def get_stream_(user_id):
    url = f"https://whowatch.tv/user/{user_id}"
    headers = {"User-Agent": "Mozzila/5.0"}
    response = requests.get(url,headers=headers)

    if response.status_code ==  200:
        soup = BeautifulSoup(response.text,"html.parser")
        m3u8_url = None
        for script in soup.find_all("script"):
            if "m3u8" in script.text:
                m3u8_url = script.text.split('"')[1]
                break
        
        return m3u8_url
    return None

user_id = "example_user"
print(get_stream_url(user_id))