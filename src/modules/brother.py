import os
from core.scraper import Scraper
import xml.etree.ElementTree as ET

class BrotherScraper(Scraper):
    def __init__(self):
        super().__init__()

    def get_counter_from_DCPL3551CDW(self):
        data = self.scrape("http://192.168.100.250/general/information.html?kind=item", "div.contentsGroup")
        path = "C:/printer-counter/archives"
        
        file_path = os.path.join(path, "brother_DCPL3551CDW.xml")
        
        raiz = ET.Element("printer_data")
        arvore = ET.ElementTree(raiz)

        for i, item_data in enumerate(data, start=1):
            item_elemento = ET.SubElement(raiz, 'item', {'id': str(i)})
            item_elemento.text = item_data

        arvore.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Dados salvos em: {file_path}")
        
        def get_item_by_id(file_path, item_id):
            tree = ET.parse(file_path)
            root = tree.getroot()

            for item in root.findall('item'):
                if item.get('id') == str(item_id):
                    return item.text

            return None

        file_path = "C:/printer-counter/archives/brother_DCPL3551CDW.xml"

        item_id = 1

        item_text = get_item_by_id(file_path, item_id)

        if item_text:
            print(f"Item com id {item_id}: {item_text}")
        else:
            print(f"Item com id {item_id} não encontrado.")