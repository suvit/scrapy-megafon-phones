# -*- coding: utf-8 -*-
from urllib import quote, urlencode
from urlparse import urljoin, urlsplit, parse_qs

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from megafon_phones.items import PhoneItem


class PhoneSpider(Spider):
    name = "megafon_phones"
    allowed_domains = ["svr.shop.megafon.ru"]
    start_urls = [
        "http://svr.shop.megafon.ru/connect/chnumber/fullnumber.html?"
        "search=1&"
        "search_area=metall&"
        "number_types_filter%5B7987%5D%5B%5D=7991&"
        "number_types_filter%5B7987%5D%5B%5D=7992&"
        "number_types_filter%5B7987%5D%5B%5D=7989&"
        "number_types_filter%5B7987%5D%5B%5D=7990",
    ]

    def parse(self, response):
        sel = Selector(response)

        for phone_sel in sel.xpath('//span[@class="g_numbers_number"]'):
            phone = PhoneItem()
            full_phone = phone_sel.xpath("text()").extract()[0].strip()
            phone['phone'] = str(full_phone).translate(None, ' -[{(\/)}]')
            yield phone

        # paging
        for page_url in sel.xpath('//div[contains(@class,"g_pages_nav")]/a/@href').extract():
            request = Request(urljoin(response.url, page_url), callback=self.parse)
            yield request
