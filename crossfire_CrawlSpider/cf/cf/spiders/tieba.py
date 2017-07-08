# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cf.items import *
from bs4 import BeautifulSoup


class TiebaSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ['baidu.com']
    base_url = 'http://tieba.baidu.com'
    start_urls = ['https://tieba.baidu.com/f?kw=' + raw_input('请输入贴吧名:')]

    rules = (
        Rule(LinkExtractor(allow=(r'/p/\d+')), callback='parse_item'),
        Rule(LinkExtractor(allow=(r'pn=\d+')), follow=True)
    )

    def parse_item(self, response):
        print '*'*50
        item = CfItem()
        soup = BeautifulSoup(response.body, 'lxml')
        # 帖子标题
        item['title'] = soup.find(class_='core_title_txt pull-left text-overflow ').get_text().strip() if soup.find(class_='core_title_txt pull-left text-overflow ') else 'NULL'
        # 回复内容
        item['comment'] = []
        floor_list = soup.find_all(class_='l_post l_post_bright j_l_post clearfix ')
        for floor in floor_list:
            each = {}
            each['floor_num'] = floor.find(class_='post-tail-wrap').contents[-2].get_text().strip() if floor.find(class_='post-tail-wrap').contents[-2] else 'NULL'
            each['date'] = floor.find(class_='post-tail-wrap').contents[-1].get_text().strip() if floor.find(class_='post-tail-wrap').contents[-1] else 'NULL'
            each['name'] = floor.find(class_='d_name').get_text().strip() if floor.find(class_='d_name') else 'NULL'
            each['level'] = floor.find(class_='p_badge').get_text().strip() if floor.find(class_='p_badge') else 'NULL'
            each['picture_link'] = floor.find(class_='BDE_Image').get('src') if floor.find(class_='BDE_Image') else 'NULL'
            item['comment'].append(each)

        yield item