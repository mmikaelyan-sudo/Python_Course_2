"""Passenger car, a vehicle with seats."""

from vehicle import Vehicle


class Car(Vehicle):
    """A passenger car.

    Attributes:
        seats: Number of seats.
    """

    def __init__(self, brand, model, year, fuel_consumption, seats=5):
        """Create a car.

        Args:
            brand: Manufacturer name, a non-empty string.
            model: Model name, a non-empty string.
            year: Production year, an int from 1886 to the current year.
            fuel_consumption: Litres per 100 km, a positive number.
            seats: Number of seats, a positive int.

        Raises:
            TypeError: If an argument has the wrong type.
            ValueError: If a string is empty, a number is out of range or
                ``seats`` is not positive.
        """
        if isinstance(seats, bool) or not isinstance(seats, int):
            raise TypeError(
                f"seats must be an int, got {type(seats).__name__}"
            )
        if seats <= 0:
            raise ValueError(f"seats must be positive, got {seats}")
        super().__init__(brand, model, year, fuel_consumption)
        self.seats = seats

    def describe(self):
        """Describe the car, including the number of seats.

        Returns:
            Text like ``Car Toyota Corolla (2015), 4 wheels, 5 seats``.
        """
        return f"{super().describe()}, {self.seats} seats"
