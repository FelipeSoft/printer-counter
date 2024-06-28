import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules.brother import BrotherScraper

def main():
    brother_DCPL3551CDW = BrotherScraper()

    # brother_DCPL3551CDW_counter = brother_DCPL3551CDW.get_counter_from_DCPL3551CDW()
    brother_DCPL3551CDW.get_counter_from_DCPL3551CDW()

    # print("Brother DCPL3551CDW:", brother_DCPL3551CDW.to_xml(brother_DCPL3551CDW_counter))

if __name__ == "__main__":
    main()