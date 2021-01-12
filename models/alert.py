import uuid
from common.database import Database
from models.item import Item
from models.model import Model


class Alert(Model):
    collection = "alerts"

    def __init__(self, item_id, price_limit, _id=None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            'item_id': self.item_id,
            'price_limit': self.price_limit,
            '_id': self._id
        }

    def load_item_price(self):
        self.item.load_price()
        return self.item.price

    def notify(self):
        if self.price_limit > self.item.price:
            print(f"Item{self.item} has reached a price under {self.price_limit}. Latest price {self.item.price}")
