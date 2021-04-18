from collections import defaultdict

class User:
    USER_DB = {}
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        self.vehicles = []
        self.ridesTaken = 0
        self.ridesOffered = 0
        User.USER_DB[name] = self
        return

    def addVehicle(self,vehicleNumber):
        self.vehicles.append(vehicleNumber)
        return 

    def __repr__(self):
        return self.name+' , '+self.age + ' , ' + str(self.vehicles) + ' \n '
        
