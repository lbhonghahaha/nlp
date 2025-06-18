import requests
import uuid
import json
from tkinter import *
def get_token(api_key, secret_key):
    URL = 'http://openapi.baidu.com/oauth/2.0/token' #百度语音识别接口
    params = {'grant_type': 'client_credentials',
              'client_id': api_key,
              'client_secret': secret_key}
    r = requests.get(URL, params=params)
    r.raise_for_status()
    token = r.json()['access_token']
    return token

def getUnit(query, service_id, api_key, secret_key,session_id):
    access_token = get_token(api_key, secret_key)
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    request = {
        "query": query,
        "user_id": "S64637",
    }
    body = {
        "log_id": str(uuid.uuid1()),
        "bot_id": service_id,
        "bot_session":json.dumps({"session_id":session_id}),
        "request": request
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, json=body, headers=headers)
        # print(response.text)
    return json.loads(response.text)
def getSession(parsed):
    if parsed is not None and 'result' in parsed:
        return json.loads(parsed["result"]['bot_session'])["session_id"]
    else:
        return ''
def getSay(parsed, intent=''):
    if parsed is not None:
        return parsed['result']['response']['action_list'][0]['say']
    else:
        return ''

def tianqichaxun(text1,text2,session_id):
        text = text1.get('1.0', END)
        parsed = getUnit(text, "1137525", 'mZ69NNk7VgLzEYVNwxIzoQtO', 'vrCHKAwDdcb6s2zGRPBuDjAwD6ucWTiZ',session_id)
        session_id = getSession(parsed)
        say = getSay(parsed)
        text2.delete('1.0', END)
        text2.insert('1.0', say)
