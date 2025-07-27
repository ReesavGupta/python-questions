from datetime import datetime
import pytest

class MaintenanceRecord:
    def __init__(self):
        self.last_service_date = datetime.now()
        self.service_history = []

    def add_service(self, description):
        self.service_history.append((datetime.now(), description))
        self.last_service_date = datetime.now()

    def get_service_history(self):
        return self.service_history

class Vehicle(MaintenanceRecord):
    id_counter = 1

    def __init__(self, make, model, year, daily_rate, fuel_type, mileage):
        super().__init__()
        self.vehicle_id = f"VH-{datetime.now().year}-{Vehicle.id_counter:04d}"
        Vehicle.id_counter += 1

        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

    def get_vehicle_info(self):
        return {
            "Vehicle ID": self.vehicle_id,
            "Make": self.make,
            "Model": self.model,
            "Year": self.year,
            "Available": self.is_available,
            "Fuel Type": self.fuel_type,
            "Mileage": self.mileage
        }


# ------------------------
# Car Class
# ------------------------
class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, fuel_type, mileage, seating_capacity, transmission_type, has_gps):
        super().__init__(make, model, year, daily_rate, fuel_type, mileage)
        self.seating_capacity = seating_capacity
        self.transmission_type = transmission_type
        self.has_gps = has_gps

    def get_fuel_efficiency(self):
        if self.transmission_type.lower() == "automatic":
            return {"city_mpg": 25, "highway_mpg": 32}
        else:
            return {"city_mpg": 30, "highway_mpg": 38}


# ------------------------
# Motorcycle Class
# ------------------------
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, fuel_type, mileage, engine_cc, bike_type):
        super().__init__(make, model, year, daily_rate, fuel_type, mileage)
        self.engine_cc = engine_cc
        self.bike_type = bike_type

    def calculate_rental_cost(self, days):
        if days < 7:
            return self.daily_rate * days * 0.8  # 20% discount
        return super().calculate_rental_cost(days)

    def get_fuel_efficiency(self):
        return {"mpg": 45}


# ------------------------
# Truck Class
# ------------------------
class Truck(Vehicle):
    def __init__(self, make, model, year, daily_rate, fuel_type, mileage, cargo_capacity, license_required, max_weight):
        super().__init__(make, model, year, daily_rate, fuel_type, mileage)
        self.cargo_capacity = cargo_capacity
        self.license_required = license_required
        self.max_weight = max_weight

    def calculate_rental_cost(self, days, commercial_use=False):
        base_cost = super().calculate_rental_cost(days)
        if commercial_use:
            return base_cost * 1.5  # 50% surcharge
        return base_cost

    def get_fuel_efficiency(self):
        return {"empty_mpg": 18, "loaded_mpg": 12}

def test_inheritance_and_instantiation():
    car = Car("Honda", "Civic", 2022, 3000, "Petrol", 15000, 5, "Automatic", True)
    assert isinstance(car, Vehicle)
    assert isinstance(car, Car)
    assert car.seating_capacity == 5
    assert car.transmission_type == "Automatic"

def test_rent_and_return():
    m = Motorcycle("Yamaha", "R15", 2021, 1000, "Petrol", 8000, 150, "Sport")
    assert m.is_available == True
    assert m.rent() == True
    assert m.is_available == False
    m.return_vehicle()
    assert m.is_available == True

def test_motorcycle_discount_rental():
    m = Motorcycle("Hero", "Splendor", 2020, 800, "Petrol", 12000, 100, "Cruiser")
    assert m.calculate_rental_cost(3) == 800 * 3 * 0.8  # Discount applied
    assert m.calculate_rental_cost(10) == 800 * 10      # No discount

def test_truck_commercial_rental():
    t = Truck("Tata", "LPT", 2019, 5000, "Diesel", 25000, 15, True, 10000)
    assert t.calculate_rental_cost(2) == 5000 * 2
    assert t.calculate_rental_cost(2, commercial_use=True) == 5000 * 2 * 1.5

def test_polymorphism_and_fuel_efficiency():
    v_list = [
        Car("Maruti", "Swift", 2021, 2000, "Petrol", 10000, 5, "Manual", False),
        Motorcycle("Bajaj", "Pulsar", 2022, 1200, "Petrol", 9000, 180, "Sport"),
        Truck("Ashok Leyland", "Boss", 2020, 6000, "Diesel", 30000, 12, True, 8000)
    ]
    assert v_list[0].get_fuel_efficiency() == {"city_mpg": 30, "highway_mpg": 38}
    assert v_list[1].get_fuel_efficiency() == {"mpg": 45}
    assert v_list[2].get_fuel_efficiency() == {"empty_mpg": 18, "loaded_mpg": 12}