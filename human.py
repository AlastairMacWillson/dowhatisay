class Human:
    default_name = None
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.age, self.name, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_age, Human.default_name)

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self,house,discount):
        price=house.final_price(discount)
        if self.__money>=price:
            self.__make_deal(house,price)
        else:
            print("U haven't money,Beeeach!")

    def __make_deal(self,house,price):
        self.__money -= price
        self.__house = house

class House:
    def __init__(self,area,price):
        self._area=area
        self._price=price

    def final_price(self,discount):
        final_price = self.price * (100 - discount)/100
        print(f'Final price:{final_price}')
        return final_price

class SmallHouse:
    default_area = 40
    def __init__(self,price):
        super().__init__(SmallHouse.default_area,price)

if __name__ == "__main__":
    Human.default_info()
    sasha=Human('Sasha',26)
    sasha.info()
    sasha.earn_money(10000)
    sasha.info()
