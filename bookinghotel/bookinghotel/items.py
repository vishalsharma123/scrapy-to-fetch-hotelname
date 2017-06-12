# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item


class BookinghotelItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_name = Field()
    time_booked = Field()
    booking_count = Field()
    strike_through_price = Field()
    discount_price = Field()
    available_rooms =Field()
    address = Field()
    region = Field()
    country = Field()
    city = Field()

    #timer=Field()

    data_list =Field()

