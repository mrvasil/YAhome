import requests
import json

def start():
    token=str(open("secrets.txt").readlines()[-1])

    name_logo_r = requests.get("https://login.yandex.ru/info", params = {"format": "json"}, headers={'Authorization': 'Bearer '+token})
    name_logo_data=json.loads(name_logo_r.text)
    name = name_logo_data["real_name"]
    img_url = f"https://avatars.yandex.net/get-yapic/{name_logo_data['default_avatar_id']}/islands-retina-middle"
    print(img_url)
    img_data = requests.get(img_url).content
    with open('interface/images/avatar.png', 'wb') as handler:
        handler.write(img_data)