# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class SakugabooruPipeline:
#     def process_item(self, item, spider):
#         return item

# sakugabooru/pipelines.py
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import os
import scrapy

class VideoDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # Atur nama file agar sesuai dengan nama video asli
        parsed_url = urlparse(request.url)
        filename = os.path.basename(parsed_url.path)
        return f"videos/{filename}"

    def get_media_requests(self, item, info):
        # Meminta unduhan dari link video yang ditemukan
        for file_url in item.get("file_urls", []):
            yield scrapy.Request(url=file_url)
