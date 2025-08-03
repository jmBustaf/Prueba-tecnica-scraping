import scrapy

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    duration = scrapy.Field()
    metascore = scrapy.Field()
    actors = scrapy.Field()
    url = scrapy.Field()
