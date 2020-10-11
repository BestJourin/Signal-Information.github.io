class Car:
    def __init__(self, mark, speed, color, price):
        self.mark = mark
        self.speed = speed
        self.color = color
        self.price = price

    def turn_to_dict(self):
        return {"mark":self.mark,
                    "speed":self.speed,
                    "color":self.color,
                    "price":self.price}
class CarInfo:
    def __init__(self):
        self.info = []
    def addcar(self, car):
        self.info.append(car.turn_to_dict())
    def getall(self):
        print(self.info)
ci = CarInfo()
car = Car('audi', 400, 'red', 100)
print(car)
ci.addcar(car)
ci.getall()