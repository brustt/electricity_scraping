from scrapy.spiders import Spider
from scrapy.http import Request
import json
from electricity_scraping.utils import *
from electricity_scraping.items import CItem

class EntsoeSpider(Spider):
    name='entsoe'
    base_url = "https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=GRAPH&areaType=BZN&atch=false&dateTime.dateTime={}|UTC|DAY&biddingZone.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A82H&resolution.values=PT15M&resolution.values=PT30M&resolution.values=PT60M&dateTime.timezone=UTC&dateTime.timezone_input=UTC"
    start_urls = []
    # catch n_days from CLI

    def start_requests(self):
        n_days = 365
        start_date = string_to_date('01.01.2019+00:00')
        self.dates = [date_to_string(_) for _ in get_date_range(start_date, n_days)]
        self.start_urls = [form_url(_, self.base_url) for _ in get_date_range(start_date, n_days)]
        for url, date in zip(self.start_urls, self.dates):
            yield Request(url=url, callback=self.parse, cb_kwargs=dict(zip(['date'],[date])))

    def parse(self, response, date):
        pattern = r'\bvar\s+chart\s*=\s*(\{.*?\})\s*;\s*\n'
        json_data = response.css('script::text').re_first(pattern)
        result = CItem()
        result['char_data'] = json.loads(json_data)['chartData']
        result['date_data'] = date
        yield result