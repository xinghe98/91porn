import scrapy
import re
from porn.items import PornItem

class PornspiderSpider(scrapy.Spider):
    name = 'PornSpider'
    allowed_domains = ['91porn.com']
    start_urls = ['https://91porn.com/v.php']

    def parse(self, response):
        items = PornItem()
        data = response.xpath('//div[@class="row"]//div[@class="row"]/div')
        for row in data:
            items['url'] = row.xpath('.//a/@href').get()
            items['title']= row.xpath('.//span[@class="video-title title-truncate m-t-5"]/text()').get()
            items['add_time'] = row.xpath('.//div').re('添加时间:</span>(.*?)<br>')[0].replace(' ','')
            items['duration'] = row.xpath('.//span[@class="duration"]/text()').get()
            info = row.xpath('.//div').get()
            items['author'] = re.findall(r'作者:</span>(.*?)<br>',info,re.S)[0].strip()
            items['views'] = re.findall(r'查看:</span> (\d+)',info)[0].strip()
            items['collect'] = re.findall(r'收藏:</span>(.*?)<br>',info,re.S)[0].strip()
            items['message'] = re.findall(r'留言:</span> (\d+)',info)[0]
            items['like'] = re.findall(r'<img src="images/like.png" .*?>(\d+)',info)[0]
            items['dislike'] = re.findall(r'<img src="images/dislike.png" .*?>(.*?)</div>',info,re.S)[0].strip()
            id = re.findall(r'id="playvthumb_(\d+)"',info)[0]
            items['video_url'] = 'https://la.killcovid2021.com/m3u8/{id}/{id}.m3u8'.format(id=id)
            yield items
            break
        next = response.xpath('//div[@id="paging"]//form/a')
        if next.xpath('.//text()').getall()[-1] == '»':
            next_page = next.xpath('.//@href').getall()[-1]
            url = 'https://91porn.com/v.php' + next_page
            yield scrapy.Request(url=url,callback=self.parse)