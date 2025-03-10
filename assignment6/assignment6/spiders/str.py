import scrapy
from assignment6.items import Assignment6Item

class StrSpider(scrapy.Spider):
    name = "str"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        assignment = Assignment6Item()
        rows = response.xpath("//*table//tbody/tr")
        for row in rows:
            assignment['number'] = row.xpath("td[1]/text()").get()
            assignment['company'] = row.xpath("td[2]/text()").get()
            assignment['symbol'] = row.xpath("td[3]/text()").get()
            assignment['ytd_return'] = row.xpath("td[4]/text()").get()
            yield assignment
