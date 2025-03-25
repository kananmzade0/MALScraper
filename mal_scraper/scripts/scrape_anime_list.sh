echo "Scraping title links..."

cd /home/kananmzade0/Projects/pythonProjects/MALScraping/mal_scraper

source .venv/bin/activate

scrapy crawl anime_list -O /home/kananmzade0/Projects/pythonProjects/MALScraper/mal_scraper/data/anime_list.json