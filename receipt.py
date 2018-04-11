import datetime
class Receipt():
    def __init__(self, taxrate):
        self.__tax_rate = taxrate
        self.__purchases = []

    def __str__(self):
        return "---- Receipt " + str(datetime.datetime.now()) + " ----"
    def addItem(self, Item):
        return self.__purchases.append(Item)
