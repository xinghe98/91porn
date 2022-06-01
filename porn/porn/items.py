# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PornItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    duration = scrapy.Field()
    views = scrapy.Field()
    message = scrapy.Field()
    collect = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
    author = scrapy.Field()
    video_url = scrapy.Field()


