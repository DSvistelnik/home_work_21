from typing import Dict

from home_work.storage_abstract import AbstractStorage
from home_work.request import Request

class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self._request = request

        self._from = storages[self._request.departure]
        self._to = storages[self._request.destination]

    def move(self):
        self._from.remove(name=self._request.product, amount=self._request.amount)
        print(f'Курьер забрал {self._request.amount} {self._request.product} из {self._request.departure}')

        print(f'Курьер везет {self._request.amount} {self._request.product}')

        self._to.add(name=self._request.product, amount=self._request.amount)
        print(f'Курьер доставил {self._request.amount} {self._request.product} в {self._request.destination}')
