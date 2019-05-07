import argparse
from AstWarpper import AstWrapper

black_list = set()
police_list = {"Т356ОК", "Richard Gross"}


class Address:
    def __init__(self, city, street, building):
        self.city = city
        self.street = street
        self.building = building


class TaxiOrder:
    def __init__(self, address):
        self.driver = None
        self.address = address
        self.client = None

    @staticmethod
    def set_driver(ord, driver):
        ord.driver = driver


class Driver:
    def __init__(self, driver_id, city, car):
        self.driver_id = driver_id
        self.city = city
        self.car = car
        self.isFree = True

    @staticmethod
    def get_car(d):
        return d.car

    @staticmethod
    def get_id(d):
        return d.driver_id

    @staticmethod
    def set_works(d):
        d.isFree = False


def block(driver):
    global black_list
    black_list.add(driver)


orders = [
    TaxiOrder(Address("Yekaterinburg", "Lenina", "2")),
    TaxiOrder(Address("Yekaterinburg", "Lenina", "101")),
    TaxiOrder(Address("Novosibirsk", "Lenina", "32")),
]

drivers = [
    Driver("John Dou", "Yekaterinburg", "Т356ОК"),
    Driver("Leo Martin", "Novosibirsk", "Х999ОК"),
    Driver("Richard Gross", "Yekaterinburg", "C000MC")
]


def find_driver(order):
    ds = []
    for d in drivers:
        if d.isFree and order.address.city == d.city:
            ds.append(d)
    return ds


def print_curr_state():
    print("SYSTEM STATE DUMP")
    print('ORDERS STATE')
    for order in orders:
        add = order.address
        dr = order.driver
        if dr is not None:
            print(f'Address: {add.city}, {add.street}, {add.building} Driver: {dr.driver_id}, {dr.city}, {dr.car}')
        else:
            print(f'Adress: {add.city} {add.street} {add.building} Driver: {dr}')
    print("BLACK LIST")
    for dr in black_list:
        print(f'Driver: {dr.driver_id}, {dr.city}, {dr.car}')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('file', default='code.txt', nargs="?",
                   help='filename with code written on this language')
    file = p.parse_args().file
    AV = AstWrapper(file)
    global_var = {
        "print": print,
        "orders": orders,
        "drivers": drivers,
        "block": block,
        "find_driver": find_driver,
        "police_list": police_list,
        "len": len,
        "black_list": black_list,
        "get_car": Driver.get_car,
        "get_id": Driver.get_id,
        "set_works": Driver.set_works,
        "set_driver": TaxiOrder.set_driver
    }
    AV.execute(global_var)
    print_curr_state()


if __name__ == "__main__":
    main()
