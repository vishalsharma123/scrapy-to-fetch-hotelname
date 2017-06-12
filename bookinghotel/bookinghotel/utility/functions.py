import scrapy
from scrapy import Selector
from bookinghotel.models import *
from bookinghotel.settings import *
import sqlalchemy.exc
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import collections



max_pages_per_hotel = 1
class W73transferAction():
    def __init__(self, items, session):
        self.items = items
        self.Session = session
        self.previous_checksum = None
        self.checksumvalues = []
        self.file_path = None
        self.w73filepath = FILES_STORE + "/W73Transfer.csv"


    pageNumber = 1

    def parse(self, response):
        for hotelurl in response.xpath('//a[@class="sr_pagination_link"]/@href'):
            url = response.urljoin(hotelurl.extract())
            yield scrapy.Request(url, callback=self.parse_hotel)

            next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')

            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)
    def parse_hotel(self, response):
            if self.pageNumber > max_pages_per_hotel:
                return
            self.data_list = []
            hxs = Selector(response)
            dict_obj = collections.OrderedDict()
            datagrid_rows_list = hxs.xpath("//span[@class='sr-hotel__name']/text()").extract()
            for i, hotellist_inner in enumerate(datagrid_rows_list):
                dict_obj = collections.OrderedDict()
                dict_obj['hotellist_inner'] = hotellist_inner
                yield self.data_list.append(dict_obj)

                next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')
                if next_page:
                   self.pageNumber += 1
                   url = response.urljoin(next_page[0].extract())
                   yield scrapy.Request(url, self.parse_hotel)

            self.ingest_w73transfer()
            return self.data_list

    def ingest_w73transfer(self):
        try:
            """Insert filtered data into the DB"""
            session = self.Session()
            print(self.data_list)
            session.bulk_insert_mappings(self.data_list)
            session.commit()


        except (Exception, sqlalchemy.exc.IntegrityError) as exc:

            session.rollback()
        finally:
            session.close()

