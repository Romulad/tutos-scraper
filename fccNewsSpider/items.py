import scrapy

class FccNewsSpiderItem(scrapy.Item):
    cover = scrapy.Field()
    tags = scrapy.Field()
    title = scrapy.Field()
    author_profile_img = scrapy.Field()
    author_name = scrapy.Field()
    created_since = scrapy.Field()
