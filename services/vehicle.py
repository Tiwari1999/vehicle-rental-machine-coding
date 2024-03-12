from models.vehicle import Vehicle


class VehicleService:
    vehicles = []

    def __init__(self, vehicle: Vehicle = None):
        self.vehicle = vehicle

    def add_vehicle(self, vehicle: Vehicle):
        """"""
        self.vehicles.append(vehicle)
        # self.append_vehicle_to_branch(vehicle)

    def append_vehicle_to_branch(self, vehicle: Vehicle):
        """"""

    def create_vehicle_object(self, *, price, branch, id, vehicle_type):
        self.get_or_create_vehicle_branch(branch)
        vehicle_ob = Vehicle(id=id, vehicle_type=vehicle_type, price=price, branch=branch)
        self.add_vehicle(vehicle_ob)
        return vehicle_ob

    def get_or_create_vehicle_branch(self, vehicle):
        """"""

    def get_all_vehicles(self):
        return self.vehicles
