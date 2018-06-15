# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    icon = scrapy.Field()
    content = scrapy.Field()
    cate_id = scrapy.Field()
    original_id = scrapy.Field()
    create_time = scrapy.Field()
    brief = scrapy.Field()
    art_source = scrapy.Field()
    click_count = scrapy.Field()
    # pass