import sys
import uuid

from models.vehicle_booking import VehicleBooking
from services.vehicle import VehicleService


class BookVehicle:
    booked_vehicles = {}

    def __init__(self, vehicle_type=None, from_time=None, to_time=None):
        self.vehicle_type = vehicle_type
        self.from_time = from_time
        self.to_time = to_time

    def get_available_vehicles_for_requested_time(self):
        """"""

    def is_vehicle_available(self, *, vehicle_id, from_time, to_time):
        """
        :param to_time:
        :param from_time:
        :param vehicle_id:
        :param *:
        """
        for k, v in self.booked_vehicles.items():
            if v.vehicle_id == vehicle_id and (
                    v.get('from_time') <= from_time <= v.get('to_time') or
                    v.get('from_time') <= to_time <= v.get('to_time')):
                """"""
                return False
        return True

    @staticmethod
    def get_all_vehicles():
        return VehicleService().get_all_vehicles()

    def rent_vehicle(self, vehicle_type, from_time, to_time):
        """"""
        all_vehicles = self.get_all_vehicles()
        booked_vehicle = None
        for vehicle in all_vehicles:
            if vehicle.type == vehicle_type and self.is_vehicle_available(vehicle_id=vehicle.id,
                                                                          from_time=from_time,
                                                                          to_time=to_time):
                if booked_vehicle is None or booked_vehicle.get('price', sys.maxsize) > vehicle.price:
                    booked_vehicle = vehicle

        if booked_vehicle:
            booked_vehicle_ob = VehicleBooking(id=uuid.uuid4(), vehicle_type=vehicle_type,
                                               from_time=from_time, to_time=to_time,
                                               price=booked_vehicle.price, vehicle_id=booked_vehicle.id)
            self.booked_vehicles.update({booked_vehicle_ob.booking_id: booked_vehicle_ob})
        return booked_vehicle

    def get_all_bookings(self):
        return self.booked_vehicles
