import requests
import json
def info1(devices_with_button, devices_with_info):
    try:
        with open('secrets.json', 'r', encoding='utf-8') as file:
            token = json.load(file)["token"]

    except FileNotFoundError:
        open("secrets.json", "w+").write("")
        token = ""

    if len(token) < 6:
        import authorization
        authorization.start()
        return 0
    

    name_logo_r = requests.get("https://login.yandex.ru/info", params = {"format": "json"}, headers={'Authorization': 'Bearer '+token})
    name_logo_data=json.loads(name_logo_r.text)
    username = name_logo_data["real_name"]
    img_url = f"https://avatars.yandex.net/get-yapic/{name_logo_data['default_avatar_id']}/islands-middle"
    img_data = requests.get(img_url).content
    with open('interface/images/avatar.png', 'wb') as handler:
        handler.write(img_data)



    dict={}
    url = 'https://api.iot.yandex.net/v1.0/user/info'
    s = requests.Session()
    headers={'Authorization': 'Bearer '+token}
    r=requests.get(url,headers=headers)
    js=json.loads(r.text)
##
    dict['devices'], dict['state'] = [], []
    dict['info'], dict['name'] = [], []
    dict['device_info'] = []
    dev=js['devices']
    for i in range(len(dev)):
        dict['devices'].append(dev[i].get('id'))
        dict['name'].append(dev[i].get('name'))
        dict['info'].append(dev[i].get('type'))

        if (dict['info'][-1] == 'devices.types.light'):
            dict['state'].append(dev[i].get("capabilities")[2].get("state").get("value"))

        if  (dict['info'][-1] == 'devices.types.socket'):
            dict['state'].append(dev[i].get("capabilities")[0].get("state").get("value"))

        if dict['info'][-1] not in devices_with_button: dict['state'].append("0")

        if dict['info'][-1] in devices_with_info: dict['device_info'].append("True")
        else: dict['device_info'].append("0")

        


##
    scenarios1=js["scenarios"]
    id, name, dict['scenarios'] = [], [], []
    for i in range(0, len(scenarios1), 1):
        id.append(scenarios1[i].get('id', 0))
        name.append(scenarios1[i].get('name', 0))
    dict['scenarios'].append(id)
    dict['scenarios'].append(name)

    dict['token']=token
    dict["username"] = username
    return dict
