import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.billboard.com/charts/billboard-200'
    ]

    def parse(self, response):
        for quote in response.xpath("//article[contains(@class, 'chart-row') and contains(@class, 'js-chart-row')]"):
            yield {
                  'rank': quote.xpath('div[@class="chart-row__primary"]//div[@class="chart-row__main-display"]//div[@class="chart-row__rank"]//span/text()').extract_first(),
                'title': quote.xpath('div[@class="chart-row__primary"]//div[@class="chart-row__main-display"]//div[@class="chart-row__container"]//div//h2/text()').extract_first(),
                'artist': quote.xpath("div[@class='chart-row__primary']//div[@class='chart-row__main-display']//div[@class='chart-row__container']//div//a/text()|div[@class='chart-row__primary']//div[@class='chart-row__main-display']//div[@class='chart-row__container']//div//h3/text()").extract_first()                
            }
