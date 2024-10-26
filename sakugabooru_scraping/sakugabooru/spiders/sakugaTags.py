# sakugabooru/spiders/sakuga_spider.py
import scrapy

class SakugaSpider(scrapy.Spider):
    name = "sakugaTag"
    tags = r"jojo%27s_bizarre_adventure_series"
    total_pages = 27
    start_urls = []
    for i in range(total_pages):
        start_urls.append(f"https://www.sakugabooru.com/post?page={i+1}&tags={tags}")
    
    def parse(self, response):
        video_links = response.css(".directlink.smallimg::attr(href)").getall()
        for video_link in video_links:
            yield {"file_urls": [video_link]}  # Send to pipeline for download



