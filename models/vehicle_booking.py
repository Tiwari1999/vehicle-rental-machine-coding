class VehicleBooking(object):
    def __init__(self, *, id, vehicle_type, from_time, to_time, price, vehicle_id):
        """
        :param *:
        """
        self.vehicle_type = vehicle_type
        self.from_time = from_time
        self.to_time = to_time
        self.price = price
        self.booking_id = id
        self.vehicle_id = vehicle_id
