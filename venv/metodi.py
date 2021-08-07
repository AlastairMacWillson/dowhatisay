class Car:
    # создание методов класса
    def __str__(self):
        return "Car class object"
    
    def start(self):
        print("Двигатель заведён")

car_a = Car()
print(car_a)
