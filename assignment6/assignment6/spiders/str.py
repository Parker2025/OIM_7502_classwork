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
            assignment['number'] = row.xpath("//table[1]//tbody/tr").get().replace('\xa0\ ', "").strip()
            assignment['company'] = row.xpath("//table[2]//tbody/tr").get().replace("\xa0\ ", "").strip()
            assignment['symbol'] = row.xpath("//table[3]//tbody/tr").get().replace("\xa0\ ", "").strip()
            assignment['ytd_return'] = row.xpath("//table[4]//tbody/tr").get().replace("\xa0\ ", "").strip()
            yield assignment
