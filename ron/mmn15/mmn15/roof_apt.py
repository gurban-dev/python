from special_apt import SpecialApt

"""
Defines the RoofApt class, a subclass of
SpecialApt with a pool attribute."""

# Import SpecialApt instead of Apt
from special_apt import SpecialApt

# Inherit from SpecialApt (since it has a view)
class RoofApt(SpecialApt):
    """
    Represents a rooftop apartment (always has a
    view, may have a pool).
    """

    # Constants
    ROOF_ADDITION = 40000
    POOL_ADDITION = 30000

    # Declare as class variable to avoid magic numbers
    VIEW_RATE = 600

    def __init__(self, floor, area, has_pool):
        """Initialize RoofApt with floor, area, and has_pool (boolean)."""

        # Call SpecialApt's init with has_view=True
        super().__init__(floor, area, has_view=True)
        if not isinstance(has_pool, bool):
            raise ValueError("has_pool must be a boolean")
        self._has_pool = has_pool

    # Getter
    def get_has_pool(self):
        """Get whether the apartment has a pool."""
        return self._has_pool

    def __eq__(self, otherRoofApt):
        """Compare if two rooftop apartments are equal (includes has_pool)."""
        if not isinstance(otherRoofApt, RoofApt):
            return NotImplemented
        return super().__eq__(otherRoofApt) and self._has_pool == otherRoofApt._has_pool

    def __str__(self):
        """A string representation including has_pool."""
        return f"{super().__str__()}, has_pool: {self._has_pool}"

    def get_price(self):
        """Calculate price including view, roof, and pool additions."""

        # Uses SpecialApt's get_price (includes view)
        base_price = super().get_price()
        roof_price = self.ROOF_ADDITION
        pool_price = self.POOL_ADDITION if self._has_pool else 0

        # No need to add view_price again
        return base_price + roof_price + pool_price