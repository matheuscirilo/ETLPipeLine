from typing import List, Dict
from bs4 import BeautifulSoup

class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        self.collect_essential_information_attributes["html"] = html
        return [{"name": 'somename',"link": 'https://somethings.com'}]


