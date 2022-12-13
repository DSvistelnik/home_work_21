from typing import  Dict
from home_work.base_storage import BaseStorage

class Store(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)