# 10. Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking
import datetime
class Car:
    kmh = 0
    def __init__(self,name) -> None:
        pass
    def accelerating(self):
        Car.kmh +=  50
        return 'Speed',Car.kmh
        
    def braking(self):
        Car.kmh == 0
        return Car.kmh

mashina = Car('maskvich')
print(mashina.accelerating())