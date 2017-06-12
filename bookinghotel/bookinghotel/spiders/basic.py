import scrapy
from bookinghotel.pipelines import *
from bookinghotel.items import BookinghotelItem

max_pages_per_hotel = 1
class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["www.booking.com"]
    start_urls = [start_url]
    custom_settings = {'ITEM_PIPELINES': {

        'bookinghotel.pipelines.BookinghotelPipeline': 300,

        'scrapy.pipelines.files.FilesPipeline': 1

    }
    }

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


        for rev in response.xpath(("//*[@id='hotellist_inner']/div")):
            item = BookinghotelItem()
            # sometimes the title is empty because of some reason, not sure when it happens but this works
            hotel_name = rev.xpath(".//a[@class='hotel_name_link url']/span[@class='sr-hotel__name']/text()")
            if hotel_name:
                item['hotel_name'] = hotel_name.extract()
            time_booked = rev.xpath(".//div[@class='rollover-s1 lastbooking']/text()")
            if time_booked:
                    item['time_booked'] = time_booked.extract()

            # strike_through_price = rev.xpath('.//td[@class="roomPrice sr_discount"]/div[@class="js_rackrate_animation_anchor smart_price_style b_bigger_tag  animated"]/span[@class="strike-it-red_anim"]/text()')
            # if strike_through_price:
            #         item['strike_through_price'] = strike_through_price.extract()
            # discount_price = rev.xpath(".//div[@class='rollover-s1 lastbooking']/text()")
            # if discount_price:
            #         item['discount_price'] = discount_price.extract()
            # available_rooms = rev.xpath('.//p[@class="review_neg"]//span/text()')
            # if available_rooms:
            #         item['available_rooms'] = available_rooms.extract()
            # address = rev.xpath('.//p[@class="review_neg"]//span/text()')
            # if address:
            #         item['address'] = address.extract()

                    yield item
        next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')
        if next_page:
                        self.pageNumber += 1
                        url = response.urljoin(next_page[0].extract())
                        yield scrapy.Request(url, self.parse_hotel)



    def parse_reviews(self, response):
        pass

