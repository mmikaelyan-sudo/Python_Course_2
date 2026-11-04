"""Truck, a vehicle that carries cargo."""

from dataclasses import dataclass, field
from typing import ClassVar

from vehicle import Vehicle


@dataclass
class Truck(Vehicle):
    """A truck whose fuel cost grows with the cargo load.

    Attributes:
        wheels: Number of wheels, overridden for trucks.
        LOAD_PENALTY: Extra fuel consumption per ton of cargo (0.1 = 10 %).
        capacity_tons: Maximum cargo in tons.
    """

    wheels: ClassVar[int] = 6
    LOAD_PENALTY: ClassVar[float] = 0.1

    capacity_tons: int
    _load: int = field(default=0, init=False, repr=False, compare=False)

    def __post_init__(self):
        """Validate the fields set by the generated constructor.

        Raises:
            TypeError: If a field has the wrong type.
            ValueError: If a base field is invalid or ``capacity_tons`` is
                not positive.
        """
        super().__post_init__()
        self._check_number(self.capacity_tons, "capacity_tons")
        if self.capacity_tons <= 0:
            raise ValueError(
                f"capacity_tons must be positive, got {self.capacity_tons}"
            )

    @property
    def load(self):
        """int: Current cargo in tons.

        Setting the load validates the new value. A failed assignment
        leaves the load unchanged.

        Raises:
            TypeError: If the new load is not a number.
            ValueError: If the new load is negative or exceeds
                ``capacity_tons``.
        """
        return self._load

    @load.setter
    def load(self, tons):
        self._check_number(tons, "load")
        if tons < 0:
            raise ValueError(f"load must not be negative, got {tons}")
        if tons > self.capacity_tons:
            raise ValueError(
                f"Overload: {tons} t exceeds capacity of "
                f"{self.capacity_tons} t"
            )
        self._load = tons

    @property
    def free_capacity(self):
        """int: Cargo in tons that still fits into the truck."""
        return self.capacity_tons - self.load

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
