# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CfItem(scrapy.Item):
    # 帖子标题
    title = scrapy.Field()
    # 回复
    comment = scrapy.Field()
        # 楼层
        #floor
        # 回复时间
        #date
        # 昵称
        #name
        # 等级
        #level
        # 回复图片
        #picture_link
