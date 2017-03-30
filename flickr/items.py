# -*- coding: utf-8 -*-
import scrapy

from pprint import pformat


class FlickrItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    image_body = scrapy.Field()

    def __str__(self):
        return pformat({
            'image_url': self['image_url'],
            'image_body': self['image_body'][:10] + '...',
        })
