from exceptions import BaseError
from home_work.courier import Courier
from home_work.request import Request
from home_work.shop import Shop
from home_work.store import Store
shop = Shop(
    items={
    "собачка": 2,
    "коробка": 5,
    },
)

store = Store(
    items={
    "печенька": 30,
    "собачка": 20,
    "коробка": 50,
    },
)
storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин." \n'
            'Введите "stop" или "стоп", чтобы продолжить:\n',
        )
        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
            courier = Courier(request=request, storages=storages)
            courier.move()

        except BaseError as error:
            print(error.massage)



if __name__ == '__main__':
    main()


