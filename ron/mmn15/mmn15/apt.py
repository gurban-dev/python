"""Defines the base Apt class for apartment properties."""

class Apt:
    """
    Represents a basic apartment with floor and area attributes.
    """

    # Constants
    PRICE_PER_SQ_METER = 20000
    FLOOR_ADDITION = 5000

    def __init__(self, floor, area):
        """
        Initialize Apt with floor and area, validating
        non-negative values.

        Note: The ground floor is floor zero and has no price charge.
        """
        if not isinstance(floor, int) or floor < 0:
            raise ValueError("Floor must be a non-negative integer")

        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Area must be a positive number")

        self._floor = floor
        self._area = area

    # Getters
    def get_floor(self):
        """Get the number of floors in the apartment."""
        return self._floor

    def get_area(self):
        """Get the area of the apartment in square meters."""
        return self._area

    def __eq__(self, otherApt):
        """Compare if two apartments are equal by floor and area."""
        if not isinstance(otherApt, Apt):
            return NotImplemented
        return self._floor == otherApt._floor and self._area == otherApt._area

    def __str__(self):
        """A string representation of the Apt object:
           floor and area."""
        return f"floor: {self._floor}, area: {self._area}"

    def get_price(self):
        """
        Calculate base price + floor addition
        (ground floor has no addition).
        """
        base_price = self._area * self.PRICE_PER_SQ_METER

        floor_price = self._floor * self.FLOOR_ADDITION if self._floor > 0 else 0

        return base_price + floor_price