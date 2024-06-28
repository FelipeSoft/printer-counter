import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

class Scraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def scrape(self, url, selector):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.select(selector)
            return [element.text.strip() for element in elements]
        else:
            return []