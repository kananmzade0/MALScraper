import scrapy

class AnimeListSpider(scrapy.Spider):
    name = "anime_list"

    def start_requests(self):
        self.limit = 0
        yield scrapy.Request(url=f"https://myanimelist.net/topanime.php?limit={self.limit}", callback=self.parse)

    def parse(self, response):
        anime_rows = response.css('tr.ranking-list')

        if not anime_rows:
            self.logger.info(f"No more anime rows found at limit={self.limit}. Stopping crawl.")
            return  # Ends the spider gracefully

        for anime in anime_rows:
            yield {
                "title": anime.css('h3 a::text').get(),
                "link": anime.css('h3 a::attr(href)').get(),
                "rank": anime.css("td.rank.ac span::text").get(),
                "score": anime.css("td.score span::text").get(),
            }

        # Follow next page if anime rows were found
        self.limit += 50
        next_url = f"https://myanimelist.net/topanime.php?limit={self.limit}"
        yield scrapy.Request(url=next_url, callback=self.parse)