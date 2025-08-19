
from special_apt import SpecialApt  # Add this import


"""
Defines the GardenApt class, a subclass of Apt
with a garden area.
"""

class GardenApt(SpecialApt):
    """
    Represents a garden apartment located on ground
    floor (floor 0) and with a garden.
    """

    def __init__(self, area, garden_area):
        """
        Initialize GardenApt with area and garden_area.
        Floor is always 0, no view allowed.
        """
        super().__init__(0, area, False)

        if not isinstance(garden_area, (int, float)) or garden_area <= 0:
            raise ValueError("Garden area must be a positive number")

        self._garden_area = garden_area

    # Getter
    def get_garden_area(self):
        """Return the area of the garden."""
        return self._garden_area

    def __eq__(self, garden_apt):
        """Check equality with another GardenApt."""
        if not isinstance(garden_apt, GardenApt):
            return NotImplemented
        return super().__eq__(garden_apt) and self._garden_area == garden_apt._garden_area

    def __str__(self):
        """A string representation including garden_area."""
        return super().__str__() + f", garden_area: {self._garden_area}"

    def get_price(self):
        """Return the price using base Apt pricing (garden does not affect price)."""
        return super().get_price()
