import uuid

from models.branch import Branch
from models.vehicle import Vehicle
from services.vehicle import VehicleService


class BranchService:
    branches = {}

    def __init__(self, branch: Branch = None):
        self.branch = branch

    def add_branch_with_city(self, branch: Branch):
        """"""
        if branch.city in self.branches:
            # Update the value for the key
            inner_dict = self.branches[branch.city]
            inner_dict[branch.name] = branch
        else:
            # Create a new inner dictionary and append it to the outer dictionary
            self.branches.update({branch.city: {branch.name: branch}})

    def add_branch(self, name, vehicles, city=None):
        """"""
        vehicles_ob = []
        for vehicle in vehicles:
            vehicle_service_ob = VehicleService()
            for i in range(vehicle.get('count')):
                ob = vehicle_service_ob.create_vehicle_object(price=vehicle.get('price'), branch=name, id=uuid.uuid4(),
                                                              vehicle_type=vehicle.get('type'))
                vehicles_ob.append(ob)
        branch = Branch(id=uuid.uuid4(), name=name, vehicles=vehicles_ob, city=city)
        self.branches.update({branch.name: branch})

    def get_branches(self):
        """"""
        return self.branches

    def get_branches_by_city(self):
        """"""

    def add_vehicle_to_branch(self, vehicle: Vehicle):
        """"""
        branch = self.branches.get(vehicle.branch, {})
        branch['vehicles'].append(vehicle)
