import datetime
class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
    def __str__(self):
        return self.__name + "____________________"  + "{:.2f}".format(self.__price)
    def getPrice(self):
        return self.__price
    def getTax(self, taxrate):
        return self.__taxrate
    


    
    
