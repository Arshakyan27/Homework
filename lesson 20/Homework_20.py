from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def get_cars_mark(self):
        pass
    
    @abstractmethod
    def beep(self):
        pass
    
    @abstractmethod
    def count_kmh(self):
        pass
    

class SportCar(Car):
    def __init__(self,name,hp):
        if not isinstance(name,str):
            raise TypeError("incorrect Type!")
        
        if not isinstance(hp,int):
            raise TypeError("incorrect Type!")
        if hp < 0:
            raise ValueError("HP should be greater than 0 !")
        self.name = name
        self.hp = hp
        
    def get_cars_mark(self):
        return f"You  are driving {self.name} ! "
    
    def beep(self):
        return "BEEEEEEEEEEEEP"
    
    def count_kmh(self):
        if self.hp <120:
            max_speed = 180
        if 120 < self.hp < 300:
            max_speed = 240
        if 300 < self.hp < 500:
            max_speed = 300
        if 500 < self.hp:
            max_speed = 350
        return max_speed
            
class Electric(Car):
    def __init__(self,name,km) -> None:
        if not isinstance(name,str):
            raise TypeError("incorrect Type!")
        
        if not isinstance(km,int):
            raise TypeError("incorrect Type!")
        if km < 0:
            raise ValueError("The range should be greater than 0 ! ")
        self.name = name
        self.km = km
        
    def beep(self):
        return "BEEEEEEEEEP"
    
    def get_cars_mark(self):
        return f"You are driving {self.name}"
    
    def count_kmh(self):
        return f"You can drive your car {self.km} kilometers! "
    
sport = SportCar("BMW",550)
electro = Electric("Tesla",450)
print(electro.count_kmh())