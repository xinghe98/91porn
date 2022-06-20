import random
from porn.units import get_proxy
import base64
import asyncio

class RandomUserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)


class ProxyMiddleware(object):

    async def process_request(self, request, spider):
        request.meta['max_retry_times'] = 10
        auth = '7894ab:bec5cc43'
        proxy =  await asyncio.create_task(get_proxy())
        request.meta['proxy'] = proxy
        auth = base64.b64encode(bytes(auth, 'utf-8'))
        request.headers['Proxy-Authorization'] = b'Basic ' + auth


