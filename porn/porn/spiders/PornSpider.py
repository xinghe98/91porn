import scrapy
import re
from porn.items import PornItem
from urllib.parse import unquote


class PornspiderSpider(scrapy.Spider):
    name = 'PornSpider'
    allowed_domains = ['91porn.com']
    start_urls = ['https://91porn.com/v.php']

    def parse(self, response):
        data = response.xpath('//div[@class="row"]//div[@class="row"]/div//a/@href').getall()
        for row in data:
            yield scrapy.Request(url=row, callback=self.parse_info)

        later = response.xpath('//div[@id="paging"]//form/a')
        if later.xpath('.//text()').getall()[-1] == '»':
            next_page = later.xpath('.//@href').getall()[-1]
            url = self.start_urls[0] + next_page
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_info(self, response):
        items = PornItem()
        items['url'] = response.request.url
        items['title'] = response.xpath('//div[@id="videodetails"][1]/h4/text()').get().strip()
        items['add_time'] = response.xpath('//span[@class="title-yakov"]/text()').get()
        video_info = response.xpath('//span[@class="video-info-span"]/text()').getall()
        items['duration'] = video_info[0]
        items['views'] = video_info[1]
        items['message'] = video_info[2]
        items['collect'] = video_info[3]
        vote = response.xpath('//div[@class="counter"]/text()').getall()
        items['like'] = vote[0]
        items['dislike'] = vote[1]
        items['author'] = []
        info = response.xpath('//div[@id="videodetails-content"]/span').get()
        author = response.xpath('//span[@class="title"]/text()').get()
        fans = re.findall(r'粉丝:(\d+)', info)[0]
        register = re.findall(r'注册:(.*前)', info)[0]
        videos = re.findall(r'<a href="uvideos.php.*?">(\d+)</a>', info)[0]
        items['author'].append({
            'author': author,
            'fans': fans,
            'register_time': register,
            'upload_video': videos
        })
        encode = response.xpath('//div[@class="video-container"]').re(r'document.write\(strencode2\((.*?)\)\)')[0]
        items['video_url'] = re.findall(r"src='(https://.*?)'", unquote(encode))[0]
        # print(items)
        yield items
