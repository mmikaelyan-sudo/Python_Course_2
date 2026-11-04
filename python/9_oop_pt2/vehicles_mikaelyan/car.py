"""Car, a passenger vehicle."""

from dataclasses import dataclass
from typing import ClassVar

from vehicle import Vehicle


@dataclass
class Car(Vehicle):
    """A passenger car with a number of seats.

    Attributes:
        FAMILY_SEATS: Minimum number of seats for a family car.
        seats: Number of seats.
    """

    FAMILY_SEATS: ClassVar[int] = 6

    seats: int = 5

    def __post_init__(self):
        """Validate the fields set by the generated constructor.

        Raises:
            TypeError: If a field has the wrong type.
            ValueError: If a base field is invalid or ``seats`` is less
                than 1.
        """
        super().__post_init__()
        if isinstance(self.seats, bool) or not isinstance(self.seats, int):
            raise TypeError(
                f"seats must be an int, got {type(self.seats).__name__}"
            )
        if self.seats < 1:
            raise ValueError(f"seats must be 1 or more, got {self.seats}")

    @property
    def is_family_car(self):
        """bool: True if the car has at least ``FAMILY_SEATS`` seats."""
        return self.seats >= self.FAMILY_SEATS

    def describe(self):
        """Describe the car, including its seats.

        Returns:
            Text like ``Car Toyota Corolla (2015), 4 wheels, 5 seats``.
        """
        return f"{super().describe()}, {self.seats} seats"
