"""Base class for all vehicles."""

import datetime


class Vehicle:
    """A generic vehicle with fuel consumption and mileage.

    Attributes:
        wheels: Number of wheels, shared by all vehicles of the class.
        fuel_price: Price of one litre of fuel in USD, shared by all
            vehicles.
        FIRST_CAR_YEAR: Earliest allowed production year.
        KM_PER_CONSUMPTION_UNIT: Distance that fuel consumption refers to.
        brand: Manufacturer name.
        model: Model name.
        year: Production year.
        fuel_consumption: Litres per 100 km.
        mileage: Kilometres driven so far.
    """

    wheels = 4
    fuel_price = 50.0
    FIRST_CAR_YEAR = 1886
    KM_PER_CONSUMPTION_UNIT = 100

    def __init__(self, brand, model, year, fuel_consumption):
        """Create a vehicle with zero mileage.

        Args:
            brand: Manufacturer name, a non-empty string.
            model: Model name, a non-empty string.
            year: Production year, an int from 1886 to the current year.
            fuel_consumption: Litres per 100 km, a positive number.

        Raises:
            TypeError: If an argument has the wrong type.
            ValueError: If a string is empty, the year is out of range or
                the fuel consumption is not positive.
        """
        self._check_text(brand, "brand")
        self._check_text(model, "model")
        self._check_year(year)
        self._check_number(fuel_consumption, "fuel_consumption")
        if fuel_consumption <= 0:
            raise ValueError(
                f"fuel_consumption must be positive, got {fuel_consumption}"
            )
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_consumption = fuel_consumption
        self.mileage = 0

    @staticmethod
    def _check_number(value, name):
        """Check that a value is an int or a float, but not a bool.

        Args:
            value: Value to check.
            name: Argument name used in the error message.

        Raises:
            TypeError: If the value is not an int or a float.
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"{name} must be a number, got {type(value).__name__}"
            )

    @staticmethod
    def _check_text(value, name):
        """Check that a value is a non-empty string.

        Args:
            value: Value to check.
            name: Argument name used in the error message.

        Raises:
            TypeError: If the value is not a string.
            ValueError: If the string is empty or contains only spaces.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"{name} must be a string, got {type(value).__name__}"
            )
        if not value.strip():
            raise ValueError(f"{name} must not be empty")

    @classmethod
    def _check_year(cls, year):
        """Check that a production year is a realistic int.

        Args:
            year: Year to check.

        Raises:
            TypeError: If the year is not an int.
            ValueError: If the year is before 1886 or in the future.
        """
        if isinstance(year, bool) or not isinstance(year, int):
            raise TypeError(f"year must be an int, got {type(year).__name__}")
        current_year = datetime.date.today().year
        if not cls.FIRST_CAR_YEAR <= year <= current_year:
            raise ValueError(
                f"year must be between {cls.FIRST_CAR_YEAR} and "
                f"{current_year}, got {year}"
            )

    def _check_distance(self, distance):
        """Check that a distance is a non-negative number.

        Args:
            distance: Distance in km.

        Raises:
            TypeError: If the distance is not a number.
            ValueError: If the distance is negative.
        """
        self._check_number(distance, "distance")
        if distance < 0:
            raise ValueError(f"distance must not be negative, got {distance}")

    @classmethod
    def set_fuel_price(cls, price):
        """Set the fuel price shared by all vehicles of the class.

        Args:
            price: New price of one litre in USD, a positive number.

        Raises:
            TypeError: If the price is not a number.
            ValueError: If the price is zero or negative.
        """
        cls._check_number(price, "price")
        if price <= 0:
            raise ValueError(f"price must be positive, got {price}")
        cls.fuel_price = price

    def drive(self, distance):
        """Add a driven distance to the mileage.

        Args:
            distance: Distance in km, a non-negative number.

        Returns:
            The new mileage in km.

        Raises:
            TypeError: If the distance is not a number.
            ValueError: If the distance is negative.
        """
        self._check_distance(distance)
        self.mileage += distance
        return self.mileage

    def trip_cost(self, distance):
        """Calculate the fuel cost of a trip.

        Args:
            distance: Distance in km, a non-negative number.

        Returns:
            The cost of the trip in USD.

        Raises:
            TypeError: If the distance is not a number.
            ValueError: If the distance is negative.
        """
        self._check_distance(distance)
        litres = (
            distance / self.KM_PER_CONSUMPTION_UNIT * self.fuel_consumption
        )
        return litres * self.fuel_price

    def describe(self):
        """Describe the vehicle.

        Returns:
            Text like ``Vehicle Toyota Corolla (2015), 4 wheels``.
        """
        return (
            f"{type(self).__name__} {self.brand} {self.model} "
            f"({self.year}), {self.wheels} wheels"
        )

    def __str__(self):
        """Return the description followed by the mileage.

        Returns:
            Text like ``Vehicle Toyota Corolla (2015), 4 wheels, 0 km``.
        """
        return f"{self.describe()}, {self.mileage} km"

    def __repr__(self):
        """Return text that looks like the constructor call.

        Returns:
            Text like ``Vehicle('Toyota', 'Corolla', 2015, 6.5)``.
        """
        return (
            f"{type(self).__name__}({self.brand!r}, {self.model!r}, "
            f"{self.year!r}, {self.fuel_consumption!r})"
        )

    def __eq__(self, other):
        """Compare two vehicles by brand, model and year.

        Args:
            other: Object to compare with.

        Returns:
            True if brand, model and year are equal, False otherwise, or
            NotImplemented if ``other`` is not a vehicle.
        """
        if not isinstance(other, Vehicle):
            return NotImplemented
        return (self.brand, self.model, self.year) == (
            other.brand,
            other.model,
            other.year,
        )
