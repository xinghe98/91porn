import random
from porn.units import proxy_url
import base64
import aiohttp
import json

class RandomUserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)


class ProxyMiddleware(object):
    proxy_url = proxy_url



    async def process_request(self, request, spider):
        request.meta['max_retry_times'] = 10
        async with aiohttp.ClientSession() as client:
            resp = await client.get(proxy_url)
            if not resp.status == 200:
                return
            res = json.loads(await resp.text())
            ip = res['data'][0]['ip']
            port = res['data'][0]['port']
            proxy = 'https://' + str(ip) + ':' + str(port)
            request.meta['proxy'] = proxy
            auths = '7894ab:bec5cc43'#代理ip服务商提供的账号密码
            auth = base64.b64encode(bytes(auths, 'utf-8'))
            request.headers['Proxy-Authorization'] = b'Basic ' + auth




class Randomip(object):
    def genip(self):
        m=random.randint(0,255)
        n=random.randint(0,255)
        x=random.randint(0,255)
        y=random.randint(0,255)
        randomIP=str(m)+'.'+str(n)+'.'+str(x)+'.'+str(y)
        return randomIP

    def process_request(self, request, spider):
        request.headers['X-Forwarded-For'] = self.genip()

