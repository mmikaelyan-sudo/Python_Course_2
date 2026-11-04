"""Demo of the Vehicle, Car and Truck classes."""

from car import Car
from truck import Truck
from vehicle import Vehicle

TRIP_KM = 200
CAR_TRIP_KM = 120
FIRST_LOAD_TONS = 10
EXTRA_LOAD_TONS = 15
NEW_FUEL_PRICE = 60


def print_trip_costs(car, truck):
    """Print the trip cost for the car and the truck.

    Args:
        car: Car to calculate the cost for.
        truck: Truck to calculate the cost for.
    """
    print(f"Car:   {car.trip_cost(TRIP_KM):.2f} USD")
    print(f"Truck: {truck.trip_cost(TRIP_KM):.2f} USD")


def main():
    """Create vehicles and show how their methods work."""
    vehicle = Vehicle("Generic", "Cart", 1999, 4.0)
    car = Car("Toyota", "Corolla", 2015, 6.5)
    truck = Truck("Volvo", "FH16", 2020, 28.0, 20)

    print("--- describe() for every vehicle ---")
    for item in [vehicle, car, truck]:
        print(item.describe())

    print("\n--- repr() and str() ---")
    print(repr(car))
    print(str(truck))

    print("\n--- drive() ---")
    print(f"Mileage after the trip: {car.drive(CAR_TRIP_KM)}")
    print(car)

    print(f"\n--- trip_cost({TRIP_KM}) ---")
    print_trip_costs(car, truck)

    print("\n--- loading the truck ---")
    print(f"Load: {truck.load_cargo(FIRST_LOAD_TONS)} t")
    print(f"Truck: {truck.trip_cost(TRIP_KM):.2f} USD")
    try:
        truck.load_cargo(EXTRA_LOAD_TONS)
    except ValueError as error:
        print(error)

    print(f"\n--- Vehicle.set_fuel_price({NEW_FUEL_PRICE}) ---")
    Vehicle.set_fuel_price(NEW_FUEL_PRICE)
    print_trip_costs(car, truck)

    print("\n--- __eq__ ---")
    same_car = Car("Toyota", "Corolla", 2015, 6.5)
    print(f"car == same_car: {car == same_car}")
    print(f"car == truck: {car == truck}")

    print("\n--- class defaults ---")
    print(f"Truck.wheels = {Truck.wheels}, Vehicle.wheels = {Vehicle.wheels}")


if __name__ == "__main__":
    main()
