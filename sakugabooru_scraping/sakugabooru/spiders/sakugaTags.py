# sakugabooru/spiders/sakuga_spider.py
import scrapy
from scrapy import Request
import urllib.parse


class SakugaSpider(scrapy.Spider):
    name = "sakugaTag"

    def start_requests(self):
        request = []
        for i in range(int(self.total_pages)):
            request.append(Request(f"https://www.sakugabooru.com/post?page={i+1}&tags={urllib.parse.quote(self.tag)}"))
        return request
    
    def parse(self, response):
        video_links = response.css(".directlink.smallimg::attr(href)").getall()
        for video_link in video_links:
            yield {"file_urls": [video_link]}  # Send to pipeline for download



