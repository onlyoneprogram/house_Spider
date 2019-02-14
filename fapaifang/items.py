# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FapaifangItem(scrapy.Item):
    # define the fields for your item here like:
    item_url = scrapy.Field()    # 各详情页链接
    title = scrapy.Field()      # 名称
    price_down = scrapy.Field()   # 起拍价
    consult_price = scrapy.Field()    # 评估价
    time_start = scrapy.Field()     # 开拍时间
    bond = scrapy.Field()      # 保证金
    price_increase = scrapy.Field()     # 加价幅度
    itemAddress = scrapy.Field()    # 地址
    area = scrapy.Field()       # 建筑面积

