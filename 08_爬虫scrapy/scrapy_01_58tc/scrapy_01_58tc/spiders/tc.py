import scrapy

class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["jingzhou.58.com"]
    start_urls = ["https://jingzhou.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_E"]

    def parse(self, response):
    # content = response.text
        # content =  response.body
        # print("======================================")
        # print(content)
        response.xpath()
