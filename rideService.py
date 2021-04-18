from user import User
from vehicle import Vehicle
from ride import Ride
from rideStrategy import RideStrategy
from vehicleConstants import VehicleConstants
from rideStatus import RideStatus
import sys

class RideService:
    
    def __init__(self):
        super().__init__()

    
    def addUser(self,name,gender,age):
        if name not in User.USER_DB:
            newUser = User(name,gender,age)
            print('User created with Name ::', newUser.name)
        else:
            print('User is already present in the DB.')
        return

    def addVehicle(self,userName,vehicleName,vehicleNumber):
        if vehicleNumber not in Vehicle.VEHICLE_DB:
            if userName not in User.USER_DB:
                print('User with given name ',userName,' does not exist.')
            else:
                user = User.USER_DB[userName]
                vehicle = Vehicle(vehicleName,vehicleNumber)
                user.vehicles.append(vehicle.vehicleNumber)
                print('Vehicle registed with vehicleNumber : ',vehicleNumber)
        else:
            print('Vehicle already present in the DB.')

        return

    # offer_ride(“Rohan, Origin=Hyderabad, Available Seats=1, Vehicle=Swift, KA-01-12345, Destination= Bangalore”)
    def offerRide(self,driverName,origin,availableSeats,vehicleName,vehicleNumber,destination):
        try:
            if driverName in User.USER_DB and vehicleNumber in User.USER_DB[driverName].vehicles:
                if (driverName,vehicleNumber) in Ride.RIDES_DB:
                    print('A ride has already been offered by this user for this vehicle.')
                else:
                    ride = Ride(driverName,origin,availableSeats,vehicleName,vehicleNumber,destination)
                    print('A new ride offering has been created by the user ', driverName)
        except:
            print("Either Driver or Vehicle doesn't exit",sys.exc_info()[0])
        return

    # select_ride(“Shashank, Origin=Mumbai, Destination=Bangalore, Seats=1, Most Vacant”)
    def selectRide(self,riderName,origin,destination,desiredSeats,selectionStrategy= RideStrategy.PREFERRED_VEHICLE,vehicleName = VehicleConstants.NONE):
        ridesList = None
        if selectionStrategy == RideStrategy.MOST_VACANT.value:
            ridesList = sorted(Ride.RIDES_DB,key=Ride.RIDES_DB.get)
        else:
            ridesList = Ride.RIDES_DB.keys()

        for ride in ridesList:
            rideValues = Ride.RIDES_DB[ride]
            if rideValues.origin == origin and rideValues.destination == destination and (rideValues.vehicleName == vehicleName or selectionStrategy == RideStrategy.MOST_VACANT.value ) and rideValues.availableSeats >= desiredSeats and rideValues.rideStatus == RideStatus.OPEN:
                rideValues.availableSeats -= 1
                rideValues.ridersName.append(riderName)
                print('Following ride has been selected :: ',rideValues)
                return 
        
        print('No rides found. Sorry!')
        return

    # endRide(“Shipra, Origin=Bangalore, Available Seats=2, Vehicle=Polo, KA-05-41491, Destination=Mysore”)
    def endRide(self,driverName,origin,availableSeats,vehicleName,vehicleNumber,destination):
        rideKey = (driverName,vehicleNumber)

        if rideKey in Ride.RIDES_DB:
            User.USER_DB[driverName].ridesOffered += 1
            Ride.RIDES_DB[rideKey].rideStatus = RideStatus.END
            ridersList = Ride.RIDES_DB[rideKey].ridersName
            for rider in ridersList:
                User.USER_DB[rider].ridesTaken += 1
            
        else:
            print('No such ride exists !!')

        return 

    def printRideStats(self):
        for key in User.USER_DB:
            user = User.USER_DB[key]
            print(user.name,':',user.ridesTaken,' Taken, ',user.ridesOffered,' Offered','\n')
        return