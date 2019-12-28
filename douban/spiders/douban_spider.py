# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["serial_number", "movie_name", "introduction", "description", "star", "evaluate"],
    }
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] =  i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            content_s = "".join(content[-1].split())
            douban_item['introduction'] = content_s
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class ='star']//span[4]/text()").extract_first()
            douban_item['description'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            # 数据yield到pipeline里进行处理/储存
            yield douban_item
        #解析下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://movie.douban.com/top250"+next_link, callback=self.parse)