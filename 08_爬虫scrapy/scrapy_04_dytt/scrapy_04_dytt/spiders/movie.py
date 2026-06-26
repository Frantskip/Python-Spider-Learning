import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dydytt.net"]
    start_urls = ["https://www.dydytt.net/index.htm"]

    def parse(self, response):
        a_list = response.xpath('//div[@class = "co_content8"]//td[@class="inddline"]/a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.dydytt.net' + href
            yield scrapy.Request(url=url,callback=self.parse_second)

    def parse_second(self,response):
        src = response.xpath('//div[@id = "Zoom"]//img/@src').extract_first()
        

