# -*- coding: utf-8 -*-
import scrapy
import json
import time
import copy
from ..items import FapaifangItem

class HouseSpiderSpider(scrapy.Spider):
    name = 'house_Spider'
    allowed_domains = ['zc-paimai.taobao.com', '203.119.244.127:80']
    start_urls = ['https://sf.taobao.com/item_list.htm?spm=a213w.7398504.miniNav.9.29ed2564P9uofu&auction_source=0'
                  '&city=%B3%C9%B6%BC&sorder=1&end_price=1000000&st_param=-1&support'
                  '_loans=1&no_buy_restrictions=1&auction_start_seg=-1']

    # start_urls = ['https://zc-paimai.taobao.com/zc_item_list.htm?'
    #               'spm=a219w.7474998.filter.104.2e605b690UeTWB&auction_'
    #               'source=0&front_category=56950002&city=%B3%C9%B6%BC&sorder=1&st_param=-1&auction_start_seg=-1']

    def parse(self, response):
        item = FapaifangItem()
        house_list = response.xpath("//script[@id='sf-item-list-data']").extract_first()
        detail = json.loads(house_list[48:-9]).get('data')
        for i in detail:
            item['item_url'] = i.get('itemUrl')
            item['title'] = i.get('title')
            item['price_down'] = i.get('initialPrice')
            item['consult_price'] = i.get('consultPrice')
            time_stamp = i.get('start')
            time_array = time.localtime(time_stamp/1000)
            item['time_start'] = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            yield scrapy.Request('https:' + item['item_url'], meta={'item': copy.deepcopy(item)}, callback=self.parse_detail, dont_filter=True)

        info = response.xpath("//div[@class='pagination J_Pagination']/a[@class='next']/@href").extract_first()
        if info:
            next_link = "".join(info.split())
            yield scrapy.Request('https:' + next_link, callback=self.parse, dont_filter=True)

        # yield item

    def parse_detail(self, response):
        item = response.meta['item']
        item['bond'] = response.xpath("//tbody[@id='J_HoverShow']/tr[2]/td[1]/span[2]/span/text()").extract_first()
        item['price_increase'] = response.xpath("//tbody[@id='J_HoverShow']/tr[1]/td[2]/span[2]/span/text()")\
            .extract_first()
        item['itemAddress'] = response.xpath("//div[@id='itemAddressDetail']/text()").extract_first()
        yield copy.deepcopy(item)



