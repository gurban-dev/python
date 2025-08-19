from roof_apt import RoofApt  # Add this import
from special_apt import SpecialApt

"""Contains utility functions for working with apartment objects."""

def average_price(apts):
    """
    Calculate the average price of a list of apartments.
    :param apts: List of apartment objects.
    :return: Average price, or 0 if the list is empty.
    """
    if not apts:
        return 0

    total_price = sum(apt.get_price() for apt in apts)

    return total_price / len(apts)

def how_many_rooftop(apts):
    """
    Count the number of rooftop apartments with a pool.
    :param apts: List of apartment objects.
    :return: Number of rooftop apartments with a pool.
    """
    return sum(
        1 for apt in apts if isinstance(apt, RoofApt) and apt.get_has_pool()
    )

def how_many_rooftop(apts):
    """
    Count the number of rooftop apartments with a pool.
    :param apts: List of apartment objects.
    :return: Number of rooftop apartments with a pool.
    """
    return sum(1 for apt in apts if isinstance(apt, RoofApt) and apt.get_has_pool())

def how_many_apt_type(apts):
    """
    Return a dictionary of apartment type counts.
    :param apts: List of apartment objects.
    :return: Dictionary with class names as keys and counts as values.
    """
    counts = {}

    for apt in apts:
        class_name = type(apt).__name__
        counts[class_name] = counts.get(class_name, 0) + 1

    return counts

def top_price(apts):
    """
    Return the apartment with the highest price.
    :param apts: List of apartment objects.
    :return: The apartment with the highest price, or None if the
             list is empty.
    """
    return max(apts, key=lambda apt: apt.get_price()) if apts else None

def only_valid_apts(apts):
    """
    Filter apartments with a view/pool and a price less than
    or equal to 1,000,000.
    :param apts: List of apartment objects.
    :return: List of valid apartments, or None if none found.
    """
    valid = [
        apt for apt in apts
        if apt.get_price() > 1_000_000 and (
            (isinstance(apt, SpecialApt) and apt.get_has_view()) or 
            (isinstance(apt, RoofApt) and apt.get_has_pool())
        )
    ]

    return valid if valid else None