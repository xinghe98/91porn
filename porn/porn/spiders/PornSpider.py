import scrapy
import re


class PornspiderSpider(scrapy.Spider):
    name = 'PornSpider'
    allowed_domains = ['91porn.com']
    start_urls = ['https://91porn.com/v.php']

    def parse(self, response):
        data = re.findall(r'<a href="(https://91porn\.com/view_video\.php\?.*?)">', response.text)
        for url in data:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        pass
