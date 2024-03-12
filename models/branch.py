class Branch(object):
    def __init__(self, id, name: str, vehicles: list, city=None):
        """"""
        self.id = id
        self.name = name
        self.vehicles = vehicles
        self.city = city
