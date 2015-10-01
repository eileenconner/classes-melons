class MelonOrder(object):


    def get_base_price(self):
        MELON_BASE_PRICE = 5.0
        
        return MELON_BASE_PRICE


class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]
    cost = 5.0


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        
        subtotal = self.cost * qty
        # purchasing 3 or more watermelons incurs a discount of 25% off
        if qty >= 3:
            return subtotal * .75
        
        return subtotal


class CantaloupeOrder(MelonOrder):
    species = "cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    cost = 5.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""
        
        subtotal = self.cost * qty
        # purchasing 5 or more cantaloupes incurs a discount of 50% off
        if qty >= 5:
            return subtotal * .5
        return subtotal


class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    cost = 6.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons orderd. """
        
        #Imported melons incure a shipping cost of 1.5* their total cost
        import_shipping = 1.5

        total = self.cost * qty * import_shipping
        
        return total


class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    cost = 5.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons orderd. """
       
        #Imported melons incure a shipping cost of 1.5* their total cost
        import_shipping = 1.5

        total = self.cost * qty * import_shipping
        
        return total


class SantaClausOrder(MelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]
    cost = 5.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons orderd. """
        
        #Imported melons incure a shipping cost of 1.5* their total cost
        import_shipping = 1.5

        total = self.cost * qty * import_shipping
        
        return total


class ChristmasOrder(MelonOrder):
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


class HornedMelonOrder(MelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    cost = 5.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        #Imported melons incure a shipping cost of 1.5* their total cost
        import_shipping = 1.5

        total = self.cost * qty * import_shipping

        return total


class XiguaOrder(MelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]
    cost = 5.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        #Imported melons incure a shipping cost of 1.5* their total cost
        import_shipping = 1.5
        # Square melons incure an extra fee of 2x the cost 
        square_fee = 2.0

        total = self.cost * qty * import_shipping * square_fee

        return total


class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    cost = 6.0


    def get_price(self, qty):
        """ Calculate price, given a number of melons ordered."""

        total = self.cost * qty

        return total