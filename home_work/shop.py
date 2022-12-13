from typing import Dict
from home_work.base_storage import BaseStorage

class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() > 5:
            ...

        super().add(name, amount)
