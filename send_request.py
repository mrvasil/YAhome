import json
import requests

def send_request(id, state, token):
    url = 'https://api.iot.yandex.net/v1.0/devices/actions'
    s = requests.Session()
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    data = '''{"devices": [{"id": "''' + id + '''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": ''' + state + '''}}]}]}'''
    r = s.post(url, headers=headers, data=data)\
    
    if (json.loads(r.text).get("devices")[0].get("capabilities")[0].get("state").get("action_result").get("status") == 'ERROR'):
        return {'res': 'error', 'text': 'Устройство не в сети', 'color': 'red'}
    else:
        if state == 'true':
            return {'res': 'successful', 'text': 'Включено', 'color': 'green'}
        else:
            return {'res': 'successful', 'text': 'Выключено', 'color': '#274dcc'}