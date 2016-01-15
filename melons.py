"""This file should have our order classes in it."""
import random

class AbstractMelonOrder(object):
    """ Abstract class for melon orders."""

    def __init__(self, species, qty):
        """Initialize unshipped melon order with melon type and number."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = random.randint(5, 9)
        self.melon_price = self.get_melon_price()

    def get_total(self):
        """Calculate price."""

        total = (1 + self.tax_rate) * self.qty * self.melon_price
        total += self.get_shipping_cost()
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

    def get_shipping_cost(self):
        """Returns shipping cost for an order."""
        return 0

    def get_melon_price(self):
        """Get melon price, taking into account individual price multipliers."""
        special_melon_multipliers = {
            "christmas" : 1.5,
        }

        mult = special_melon_multipliers.get(self.species.lower(), 1)
        return mult * self.base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """Class representing a domestic melon order."""
    order_type = "domestic"
    tax_rate = 0.08
    country_code = 'USA'


class InternationalMelonOrder(AbstractMelonOrder):
    """Class representing a international melon order."""
    order_type = "international"
    tax_rate = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize international unshipped order with melon type, number, country code."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_shipping_cost(self):
        """Returns international shipping cost for an order."""
        if self.qty < 10:
            return 3

        return 0


class GovernmentMelonOrder(AbstractMelonOrder):
    """Class representing a government melon order."""
    order_type = "government"
    tax_rate = 0.00
    country_code = 'USA'

    def __init__(self, species, qty):
        """Initialize government unshipped order with melon type, number, country code."""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def inspect_melons(self, passed):
        """Set inspection results to provided value."""
        self.passed_inspection = passed
