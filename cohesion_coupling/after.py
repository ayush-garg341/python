"""
    In every software , there must be
        1. Should have High Cohesion -> all related responsibilities in one class.
        2. Should have Low Coupling -> all un-related things are in different class. 
"""

import random
import string


class VehicleInfo:

    brand: str
    electric: bool
    catalogue_price: float

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        return self.catalogue_price * tax_percentage

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:

    vehicle_id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, vehicle_id, license_plate, info) -> None:
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print("Vehicle Id : ", self.vehicle_id)
        print("Vehicle License Plate : ", self.license_plate)
        self.info.print()


class VehicleRegistry:
    def __init__(self) -> None:
        self.vehicle_info = {}
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def vehicle_license_plate(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.vehicle_id(12)
        license_plate = self.vehicle_license_plate(vehicle_id)
        info = self.vehicle_info[brand]

        return Vehicle(vehicle_id, license_plate, info)


class Application:
    def register_vehicle(self, brand):
        vehicle = VehicleRegistry()
        return vehicle.create_vehicle(brand)


car = Application()
vehicle = car.register_vehicle("BMW 5")
vehicle.print()
