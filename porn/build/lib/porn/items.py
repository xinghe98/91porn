# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PornItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    add_time = scrapy.Field()
    duration = scrapy.Field()
    author = scrapy.Field()
    views = scrapy.Field()
    message = scrapy.Field()
    collect = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
    video_url = scrapy.Field()


