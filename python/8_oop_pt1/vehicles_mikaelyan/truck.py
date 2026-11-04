"""Truck, a vehicle that carries cargo."""

from vehicle import Vehicle


class Truck(Vehicle):
    """A truck whose fuel cost grows with the cargo load.

    Attributes:
        wheels: Number of wheels, overridden for trucks.
        LOAD_PENALTY: Extra fuel consumption per ton of cargo (0.1 = 10 %).
        capacity_tons: Maximum cargo in tons.
        load: Current cargo in tons.
    """

    wheels = 6
    LOAD_PENALTY = 0.1

    def __init__(self, brand, model, year, fuel_consumption, capacity_tons):
        """Create an empty truck.

        Args:
            brand: Manufacturer name, a non-empty string.
            model: Model name, a non-empty string.
            year: Production year, an int from 1886 to the current year.
            fuel_consumption: Litres per 100 km, a positive number.
            capacity_tons: Maximum cargo in tons, a positive number.

        Raises:
            TypeError: If an argument has the wrong type.
            ValueError: If a string is empty, a number is out of range or
                ``capacity_tons`` is not positive.
        """
        self._check_number(capacity_tons, "capacity_tons")
        if capacity_tons <= 0:
            raise ValueError(
                f"capacity_tons must be positive, got {capacity_tons}"
            )
        super().__init__(brand, model, year, fuel_consumption)
        self.capacity_tons = capacity_tons
        self.load = 0

    def load_cargo(self, tons):
        """Add cargo to the truck.

        Args:
            tons: Cargo to add in tons, a non-negative number.

        Returns:
            The new load in tons.

        Raises:
            TypeError: If ``tons`` is not a number.
            ValueError: If ``tons`` is negative or the new load would
                exceed the capacity. The load stays unchanged.
        """
        self._check_number(tons, "tons")
        if tons < 0:
            raise ValueError(f"tons must not be negative, got {tons}")
        new_load = self.load + tons
        if new_load > self.capacity_tons:
            raise ValueError(
                f"Overload: {new_load} t exceeds capacity of "
                f"{self.capacity_tons} t"
            )
        self.load = new_load
        return self.load

    def unload(self):
        """Remove all cargo from the truck."""
        self.load = 0

    def trip_cost(self, distance):
        """Calculate the fuel cost of a trip with the current load.

        Args:
            distance: Distance in km, a non-negative number.

        Returns:
            The cost of the trip in USD, increased by 10 % per ton.

        Raises:
            TypeError: If the distance is not a number.
            ValueError: If the distance is negative.
        """
        return super().trip_cost(distance) * (
            1 + self.LOAD_PENALTY * self.load
        )

    def describe(self):
        """Describe the truck, including its load.

        Returns:
            Text like ``Truck Volvo FH16 (2020), 6 wheels, 0/20 t``.
        """
        return f"{super().describe()}, {self.load}/{self.capacity_tons} t"
