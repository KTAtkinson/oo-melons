"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """ Abstract class for melon orders."""

    def __init__(self, species, qty):
        """Initialize unshipped melon order with melon type and number."""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax_rate) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


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
