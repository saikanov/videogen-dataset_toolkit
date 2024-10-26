import scrapy
from scrapy import Request

class SakugaSpider(scrapy.Spider):
    name = "sakugaPools"

    def start_requests(self):
        request = []
        for i in range(int(self.total_pages)):
            request.append(Request(f"https://www.sakugabooru.com/pool/show/{self.PoolID}?page={i}"))
        return request
            
    def parse(self, response):
        # Get all thumbnail links
        post_links = response.css("a.thumb::attr(href)").getall()

        for post_link in post_links:
            # Make sure the URL is absolute
            full_url = f"https://www.sakugabooru.com{post_link}"
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_pool
            )

    def parse_pool(self, response):
        
        # Get video links
        video_links = response.css("video source::attr(src)").get()
        if video_links:
            yield {
                "file_urls": [video_links]
            }