import scrapy

class TeoniteSpider(scrapy.Spider):
    name='teonite'
    allowed_domains = ['teonite.com']


    def start_requests(self):
        yield scrapy.Request('http://teonite.com/blog/', callback=self.parse_first_url)

    def parse_first_url(self, response):
        first_url=response.css('h2.post-title a::attr(href)').extract_first()
        yield scrapy.Request('http://teonite.com%s' % first_url, callback=self.parse)

    def parse(self, response):
        item=PostItem()
        item['author']=response.css('span.author-content h4::text').extract_first()
        item['post']=response.css("section.post-content *::text").extract()
        next_page=response.css('li.pull-left a::attr(href)').extract_first()
        item['link']=response.url
        yield item

        if next_page is not None:
            next_page='http://'+self.allowed_domains[0]+next_page
            yield scrapy.Request(next_page, callback=self.parse)
