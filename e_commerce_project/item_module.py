class Item_package:

    def __int__(self):
        self.item_id = None
        self.item_descr = None
        self.item_quanity = None
        self.item_price = None

    def discounted_price(self):
        if self.item_quanity == 2:
            self.item_price = (self.item_price - ((10 / 100) * self.item_price))*self.item_quanity
        elif self.item_quanity <= 3 and self.item_quanity >= 5:
            self.item_price = (self.item_price - ((15 / 100) * self.item_price))*self.item_quanity
        elif self.item_quanity >= 6:
            self.item_price = (self.item_price - ((25 / 100) * self.item_price))*self.item_quanity
        else:
            print(self.item_price, " - no discount")