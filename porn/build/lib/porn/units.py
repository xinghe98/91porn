import json
import asyncio
import aiohttp


async def get_proxy():
    url = 'http://api.ipipgo.com/ip?cty=SG,TW,JP,HK&c=1&pt=1&ft=json&rep=2&key=93cc1773&ts=10'
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            res = json.loads(await resp.text())
            if res['code'] == 200:
                ip = res['data'][0]['ip']
                port = res['data'][0]['port']
                proxy = 'https://' + str(ip) + ':' + str(port)
                print(proxy)
                return proxy
            else:
                print('代理出问题了' + str(res['code']))
                get_proxy()


MONGO_URI = 'mongodb://127.0.0.1:27017/'
