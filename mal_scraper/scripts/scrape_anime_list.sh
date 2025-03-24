echo "Scraping title links..."

cd /home/kananmzade0/Projects/pythonProjects/MALScraping/mal_scraper

source venv/bin/activate

scrapy crawl anime_scraper -O ../data/anime_list.json