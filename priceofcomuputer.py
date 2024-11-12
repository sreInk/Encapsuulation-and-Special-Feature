class Computer:
    def __init__(self) :
        self.__maxprice = 900
    
    def sell(self):
        print("Selling is {}".format(self.__maxprice))
    def setmax(self,price):
        self.__maxprice = price
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setmax(1000)
c.sell()
