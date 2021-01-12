from typing import Dict
import uuid
import re
import requests
from bs4 import BeautifulSoup
from common.database import Database
from models.model import Model


class Item(Model):
    collection = "items"

    def __init__(self, url: str, query: Dict, tag: str, _id: str = None):
        super().__init__()
        self.url = url
        self.query = query
        self.tag = tag
        self.price = None
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"url: {self.url}"

    def load_price(self) -> float:

        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find(self.tag, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d*,?\d*\.\d\d)")
        match = pattern.search(string_price)
        found_p = match.group(1)
        self.price = float(found_p.replace(',', ''))
        return self.price

    def json(self) -> Dict:
        return{
            'url': self.url,
            'query': self.query,
            'tag': self.tag,
            '_id': self._id
        }

