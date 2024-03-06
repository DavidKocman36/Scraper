import scrapy

class RealitySpider(scrapy.Spider):
    name = "Spider"
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&tms=1709636083199']

    def parse(self, response):

        for estate in response.json()["_embedded"]["estates"]:
            yield {
                "name": estate["name"],
                "images": estate["_links"]["images"]
            }