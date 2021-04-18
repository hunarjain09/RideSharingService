from rideStatus import RideStatus

class Ride:

    RIDES_DB = {}
    def __init__(self,driverName,origin,availableSeats,vehicleName,vehicleNumber,destination):
        self.driverName = driverName
        self.vehicleName = vehicleName
        self.vehicleNumber = vehicleNumber
        self.origin = origin
        self.destination = destination
        self.availableSeats = availableSeats
        self.ridersName = []
        self.rideStatus = RideStatus.OPEN
        Ride.RIDES_DB[(driverName,vehicleNumber)] = self 
        
        return
    
    def __lt__(self, other):
        if self.availableSeats > other.availableSeats:
            return True
        return False

    def __repr__(self):
        return self.driverName+' , '+str(self.rideStatus.value) + ' , ' + self.vehicleNumber + ' , ' + str(self.ridersName) + ' \n '

    

    
