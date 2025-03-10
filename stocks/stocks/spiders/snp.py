import scrapy


class SnpSpider(scrapy.Spider):
    name = "snp"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"]

    def parse(self, response):
        symbol = response.xpath("//table[@id = 'constituents']//td[1]/text()").get()
        return {"symbol": symbol}
