# 1. Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule



class Hospital:
    schedule = {}
    def __init__(self,patient) -> None:
        self.patient = patient
        
    def scheduling(self,time):
        
        self.time = time
        Hospital.schedule[self.patient] = self.time
        return f'You are scheduled for {self.time} ! '

        
    
    def remove_schedule(self,time):
        if not isinstance(time,int):
            raise TypeError("Wrong Type !")
        self.time = time
        return f'You removed your scheduled time !  '
    
pacient = Hospital('Vahag')
print(pacient.scheduling('12:00'))