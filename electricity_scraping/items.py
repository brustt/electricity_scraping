from dataclasses import Field, dataclass
from typing import List
from scrapy import Item, Field

class CItem(Item):
    char_data = Field()
    date_data = Field()