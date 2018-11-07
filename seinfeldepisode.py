import scrapy

class SeinfeldEpisodeSpider(scrapy.Spider):
    #run from commandline
    #scrapy runspider seinfeldepisode.py -t json --nolog -o - > episode.json

    name = 'seinfeldepisodespider'
    # start_urls = ['http://www.seinfeldscripts.com/']

    # Add a custom constructor with the url parameter
    def __init__(self, start_urls='http://www.example.com', *args, **kwargs):
        # Don't forget to call parent constructor
        super(SeinfeldEpisodeSpider, self).__init__(*args, **kwargs)
        # Set the start_urls to be the one given in url parameters
        self.start_urls = [start_urls]

    def parse(self, response):
        content = response.css('div#content')
        yield {
            'title': content.css('h1 ::text').extract_first()
            }
        for line in response.css('p'):
            yield {
                'line': line.css('::text').extract()
            }
