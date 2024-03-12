class Vehicle(object):
    def __init__(self, *, id, vehicle_type, price, branch):
        """
        :param *:
        """
        self.price = price
        self.branch = branch
        self.id = id
        self.type = vehicle_type
