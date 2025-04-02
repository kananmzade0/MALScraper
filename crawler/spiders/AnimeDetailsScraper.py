import json
import scrapy

class AnimeDetailsScraper(scrapy.Spider):
    name = "anime_details"

    def start_requests(self):
        with open('mal_scraper/data/anime_list.json', 'r') as f:  #/home/kananmzade0/Projects/pythonProjects/MALScraping/anime_list.json
            anime_list = json.load(f)
            for anime in anime_list:
                yield scrapy.Request(url=anime['link'], callback=self.parse_anime)

    def parse_anime(self, response):
        yield {
            # Top of the page
            "title": response.css('h1.title-name strong::text').get(),


            # Synopsis
            "synopsis": response.css('p[itemprop="description"]::text').get(),

            # Information
            "type": response.xpath('//span[text()="Type:"]/following-sibling::a/text()').get(),
            "episodes": response.xpath('//span[text()="Episodes:"]/following-sibling::text()').get(),
            "status": response.xpath('//span[text()="Status:"]/following-sibling::text()').get(),
            "aired": response.xpath('//span[text()="Aired:"]/following-sibling::text()').get(),
            "premiered": response.xpath('//span[text()="Premiered:"]/following-sibling::a/text()').get(),
            "broadcast": response.xpath('//span[text()="Broadcast:"]/following-sibling::text()').get(),
            "producers": response.xpath('//span[text()="Producers:"]/following-sibling::a/text()').getall(),
            "licensors": response.xpath('//span[text()="Licensors:"]/following-sibling::a/text()').getall(),
            "studios": response.xpath('//span[text()="Studios:"]/following-sibling::a/text()').getall(),
            "source": response.xpath('//span[text()="Source:"]/following-sibling::a/text()').get(),
            "genres": response.xpath('//span[text()="Genres:"]/following-sibling::a/text()').getall(),
            "demographic": response.xpath('//span[text()="Demographic:"]/following-sibling::a/text()').getall(),
            "themes": response.xpath('//span[text()="Theme:"]/following-sibling::a/text()').getall(),
            "duration": response.xpath('//span[text()="Duration:"]/following-sibling::text()').get(),
            "rating": response.xpath('//span[text()="Rating:"]/following-sibling::text()').get(),

            # Statistics
            "score": response.css('span[itemprop="ratingValue"]::text').get(),
            "ranked": response.xpath('//span[text()="Ranked:"]/following-sibling::text()').get(),
            "popularity": response.xpath('//span[text()="Popularity:"]/following-sibling::text()').get(),
            "members": response.xpath('//span[text()="Members:"]/following-sibling::text()').get(),
            "favorites": response.xpath('//span[text()="Favorites:"]/following-sibling::text()').get(),

            # Link
            "link": response.url
        }