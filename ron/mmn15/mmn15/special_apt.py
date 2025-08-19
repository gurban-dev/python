from apt import Apt

"""Defines the SpecialApt class, a subclass of Apt with a view attribute."""

class SpecialApt(Apt):
    """Represents a special apartment with a view."""
    VIEW_ADDITION = 600

    def __init__(self, floor, area, has_view):
        """
        Initialize SpecialApt with floor, area, and whether it has a view.
        """
        super().__init__(floor, area)
        if not isinstance(has_view, bool):
            raise ValueError("has_view must be a boolean")
        self._has_view = has_view

    # Getter
    def get_has_view(self):
        """Return True or False depending on whether this
           apartment has a view."""
        return self._has_view

    def get_price(self):
        """
        Calculate price including base price + view
        premium (if applicable).
        """
        base_price = super().get_price()
        view_price = self._floor * self.VIEW_ADDITION if self._has_view and self._floor > 0 else 0

        return base_price + view_price

    def __eq__(self, other):
        """Check equality with another SpecialApt."""
        if not isinstance(other, SpecialApt):
            return NotImplemented
        return super().__eq__(other) and self._has_view == other._has_view

    def __str__(self):
        """A string representation including has_view."""
        return f"{super().__str__()}, has_view: {self._has_view}"