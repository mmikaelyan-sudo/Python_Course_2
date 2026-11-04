"""Demonstrate the Vehicle, Car and Truck dataclasses."""

from car import Car
from truck import Truck
from vehicle import Vehicle

TRIP_KM = 200


def main():
    """Create vehicles and print their behaviour step by step."""
    cart = Vehicle("Generic", "Cart", 1999, 4.0)
    car = Car("Toyota", "Corolla", 2015, 6.5)
    truck = Truck("Volvo", "FH16", 2020, 28.0, 20)

    print("--- describe() for every vehicle ---")
    for vehicle in (cart, car, truck):
        print(vehicle.describe())

    print("\n--- generated repr() and our str() ---")
    print(repr(car))
    print(str(truck))

    print("\n--- __post_init__ validation ---")
    try:
        Vehicle("Ford", "Model T", 1800, 12.0)
    except ValueError as error:
        print(error)

    print("\n--- read-only property mileage ---")
    print(f"Mileage after the trip: {car.drive(120)}")
    print(car)
    try:
        car.mileage = 0
    except AttributeError:
        print("mileage is read-only, use drive()")

    print("\n--- computed properties ---")
    print(f"full_name: {car.full_name}")
    print(f"is_family_car: {car.is_family_car}")
    print(f"free_capacity: {truck.free_capacity} t")

    print(f"\n--- trip_cost({TRIP_KM}) ---")
    print(f"Car:   {car.trip_cost(TRIP_KM):.2f} USD")
    print(f"Truck: {truck.trip_cost(TRIP_KM):.2f} USD")

    print("\n--- property setter load ---")
    truck.load = 10
    print(f"Load: {truck.load} t, free: {truck.free_capacity} t")
    print(f"Truck: {truck.trip_cost(TRIP_KM):.2f} USD")
    try:
        truck.load += 15
    except ValueError as error:
        print(error)
    print(truck.describe())

    print("\n--- Vehicle.set_fuel_price(60) ---")
    Vehicle.set_fuel_price(60)
    print(f"Car:   {car.trip_cost(TRIP_KM):.2f} USD")
    print(f"Truck: {truck.trip_cost(TRIP_KM):.2f} USD")

    print("\n--- generated __eq__ ---")
    same_car = Car("Toyota", "Corolla", 2015, 6.5)
    print(f"car == same_car: {car == same_car}")
    print(f"car == truck: {car == truck}")

    print("\n--- class defaults ---")
    print(f"Truck.wheels = {Truck.wheels}, Vehicle.wheels = {Vehicle.wheels}")


if __name__ == "__main__":
    main()
