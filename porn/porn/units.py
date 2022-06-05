import requests
import json


def get_proxy():
    response = requests.get('http://api.ipipgo.com/ip?cty=00&c=1&pt=1&ft=json&pat=\n&rep=1&key=93cc1773&ts=3').text
    res = json.loads(response)
    if res['code'] == 200:
        print(res['data'])
        ip = res['data'][0]['ip']
        port = res['data'][0]['port']
        proxy = 'https://' + str(ip) + ':' + str(port)
        return proxy
    else:
        print('代理出问题了' + res['code'])
