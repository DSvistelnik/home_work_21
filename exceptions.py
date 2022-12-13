class BaseError(Exception):
    massage = 'Неизвестная ошибка'


class NotEnoughError(BaseError):
    massage = 'Недостаточно места'

class UnknownProductError(BaseError):
    massage = 'Неизвестный товар'

class NotEnoughProductError(BaseError):
    massage = 'Недостаточно товара'

class InvalidRequestError(BaseError):
    massage = 'Неправильный запрос'

class UnknownStorageError(BaseError):
    massage = 'Неизвестный склад'