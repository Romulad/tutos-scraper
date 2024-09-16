from typing import Any
import scrapy
from scrapy.http import Response

from ..constant import FCC_NEWS_SPIDER_NAME


class FccNewsSpider(scrapy.Spider):
    name = FCC_NEWS_SPIDER_NAME
    base_url = "https://www.freecodecamp.org/"
    start_urls = [
        "https://www.freecodecamp.org/news/"
    ]
    
    def parse(self, response: Response) -> Any:
        post_card_list_css_selector = ".post-feed .post-card"
        post_card_article_path = ".post-card-image-link::attr(href)"
        post_card_atricle_cover = ".post-card-image-link img::attr(src)"
        post_tags = ".post-card-content .post-card-tags a::text"
        post_title = ".post-card-content .post-card-title a::text"
        post_author_name = ".meta-content a::text"
        post_author_img = ".static-avatar img::attr(src)"
        post_since_created = ".meta-content time::text"
        post_create_at = ".meta-content time::attr(datetime)"