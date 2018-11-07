import scrapy

class SeinfeldEpisodesSpider(scrapy.Spider):
    #run from commandline
    #scrapy runspider seinfeldepisodes.py -t json --nolog -o - > seinfeldepisodes.json

    name = 'seinfeldepisodesspider'
    start_urls = ['http://www.seinfeldscripts.com/seinfeld-scripts.html']

    def parse(self, response):
        content = response.css('div#content')
        table = content.css('table tbody tr')

        episodehtml = table.css('td a')
        links = episodehtml.css('::attr(href)').extract()

        episodes = table.css('td ::text').extract()
        #remove empty text, season headers and pilot header (episodes named pilot so be careful)
        episodes = [x for x in episodes if not ( x.isspace() or 'Season' in x or '(1989)' in x)]
        i = 0
        count = 0
        while i < len(episodes):
            yield {
                'number': episodes[i].strip(),
                'name': episodes[i + 1].strip(),
                'date': episodes[i + 2].strip(),
                'link': links[count].strip()
            }
            i += 3
            count += 1
