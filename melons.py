"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"

    def __init__(self, species, qty, tax=0.08):
        """Initialize melon order attributes."""

        self.tax = tax
        return super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"

    def __init__(self, species, qty, country_code, tax=0.17):
        """Initialize melon order attributes."""

        self.country_code = country_code
        self.tax = tax
        return super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order1 = DomesticMelonOrder("cantaloupe", 8)
order0 = InternationalMelonOrder("watermelon", 6, "AUS")
order2 = InternationalMelonOrder("watermelon", 16, "AUS")
order3 = DomesticMelonOrder("Christmas melon", 8)
order4 = InternationalMelonOrder("Christmas melon", 6, "AUS")
