# This is a sample Python script.
import uuid

from services.book_vehicle import BookVehicle
from services.branch import BranchService
from services.users import UserService
from services.vehicle import VehicleService


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    branch_service = BranchService()
    user_service = UserService()
    vehicle_service = VehicleService()
    book_vehicle = BookVehicle()

    branch_service.add_branch('gachibowli', [{'type': 'suv', 'count': 1, 'price': 12},
                                             {'type': 'sedan', 'count': 3, 'price': 10},
                                             {'type': 'bike', 'count': 3, 'price': 20}], 'bangalore')

    # vehicle_service.create_vehicle_object(price=11, branch='miapur', id=uuid.uuid4(), vehicle_type='sedan')
    vehicle_service.create_vehicle_object(price=11, branch='gachibowli', id=uuid.uuid4(), vehicle_type='sedan')
    branch_service.add_branch('miapur', [{'type': 'suv', 'count': 1, 'price': 12},
                                         {'type': 'sedan', 'count': 3, 'price': 10},
                                         {'type': 'bike', 'count': 3, 'price': 20}], 'bangalore')
    # print(branch_service.get_branches())
    for k, v in branch_service.get_branches().items():
        print(k, "the value is")
        print(v.__dict__)

    for v in vehicle_service.get_all_vehicles():
        print(v.__dict__)
    # print(vehicle_service.get_all_vehicles())

    book_vehicle.rent_vehicle('suv', 10, 12)
    book_vehicle.rent_vehicle('suv', 10, 12)
    for k, v in book_vehicle.get_all_bookings().items():
        print("th booking is")
        print(k, " the value is")
        print("the value is", v.__dict__)

    # book_vehicle.rent_vehicle()
    # book_vehicle.rent_vehicle()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
