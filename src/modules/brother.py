from core.scraper import Scraper
# http://192.168.100.250/
class BrotherScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.amazon.com.br/s?k=notebook'
        self.selector = 'span.a-price-whole'

    def get_counter_from_DCPL3551CDW(self):
        return self.scrape(self.url, self.selector)
