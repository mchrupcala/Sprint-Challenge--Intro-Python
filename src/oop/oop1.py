# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# 'Vehicle' is the base class
class Vehicle:
    def __init__(self, vehicles=[]):
        self.vehicles = [FlightVehicle, GroundVehicle]

class FlightVehicle(Vehicle):
    def __init__(self, vehicle_types=[]):
        self.vehicle_types = [Starship, Airplane]

class Starship(FlightVehicle):
    def __init__(self, vehicles=None):
        self.vehicles = vehicles

class Airplane(FlightVehicle):
    def __init__(self, vehicles=None):
        self.vehicles = vehicles


class GroundVehicle(Vehicle):
    def __init__(self, vehicles=[]):
        self.vehicles = [Car, Motorcycle]

class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

