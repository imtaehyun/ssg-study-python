#-*-coding: utf-8
import scrapy


class SpaekerInfoSpider(scrapy.Spider):
    name = "speaker_info"

    start_urls = [
        'https://www.pycon.kr/2017/program/speaker/'
    ]

    def parse(self, response):
        """
        filename = 'pycon_speaker_change.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        """
        for speaker_info in response.css("div.media-body"):
            yield{
                'name' : speaker_info.css("h4.media-heading a::text").extract_first(),
                'link' : speaker_info.css("a.btn-social::attr(href)").extract()
            }
