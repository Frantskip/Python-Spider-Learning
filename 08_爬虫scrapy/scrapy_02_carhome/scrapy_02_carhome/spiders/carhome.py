import scrapy
from lxml import etree

class CarhomeSpider(scrapy.Spider):
    name = "carhome"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/cars/brand-15-x-x-x-x-1.html"]

    def parse(self, response):
        name_list = response.xpath('//div[@data-selected="false"]//div//@title')
        for name in name_list.getall():
            print(name.extract())

