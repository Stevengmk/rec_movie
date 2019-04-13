# -*- coding: utf-8 -*-
import scrapy
from spider.items import SpiderItem

class SportSpider(scrapy.Spider):
    # 爬虫名，该值必须唯一
    name = "teacher"
    # 爬虫的爬取域(我要拿传智的数据)
    allowed_domains = ["itcast.cn"]
    # 起始的URL列表，也就是第一批请求的地址
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml"
    ]

    # pase方法负责解析返回的数据response data、获得要提取的数据item，以及生成需要进一步处理URL的Request对象。
    def parse(self, response):
        # 获取的数据集
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = SpiderItem()
            # .extract()将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # yield ：获得一个item数据后暂停循环，然后将它交给管道，之后继续进行循环
            yield item


    # def parse(self, response):
    #     node_list = response.xpath("div[@class='list']")
    #     for node in node_list:
    #         item = SpiderItem()
    #         date = node.xpath("./h3/text()").extract()
    #         time = node.xpath("li[@time]").extract()
    #         title = node.xpath("li[@label]").extract()
    #         item['data'] = date[0]
    #         item['time'] = time[0]
    #         item['title'] = title[0]
    #         yield item
