"""
    This code has very low cohesion and very high coupling.
    
    1. If we change the VehicleRegistry class, we need to change in register_vehicle of Application.
    2. it is hard to add new brand category....
    3. We are calculating the tax in same class....
"""

import random
import string

class VehicleRegistry:

    def vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k = length))

    def vehicle_license_plate(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:

    def register_vehicle(self, brand):

        registry = VehicleRegistry()

        vehicle_id = registry.vehicle_id(12)

        license_plate = registry.vehicle_license_plate(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


car = Application()
car.register_vehicle("BMW 5")

