"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0   # TODO, calculate the real amount!

        return total


class CantaloupeOrder(object):
    species = "cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = 0

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):
        """ Calculate price, given a number of melons orderd. """
        total = 0
        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):

        total = 0
        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        total = 0
        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["winter"]
    cost = 5.0

    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = self.cost * qty

        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = 0

        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = 0

        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = 0

        return total