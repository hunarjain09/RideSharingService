from rideService import RideService
from user import User
from vehicle import Vehicle
from ride import Ride

rideService = RideService()

rideService.addUser('Rohan', 'M', '36') 
rideService.addVehicle('Rohan', 'Swift', 'KA-01-12345')

rideService.addUser('Shashank', 'M', '29')
rideService.addVehicle('Shashank', 'Baleno', 'TS-05-62395')

rideService.addUser('Nandini', 'F', '29')  

rideService.addUser('Shipra', 'F', '27')
rideService.addVehicle('Shipra', 'Polo', 'KA-05-41491')
rideService.addVehicle('Shipra', 'Activa', 'KA-12-12332')

rideService.addUser('Gaurav', 'M', '29')

rideService.addUser('Rahul', 'M', '35')
rideService.addVehicle('Rahul', 'XUV', 'KA-05-1234')

# print(User.USER_DB)


rideService.offerRide('Rohan', 'Hyderabad', 1, 'Swift', 'KA-01-12345', 'Bangalore')

rideService.offerRide('Shipra', 'Bangalore', 1, 'Activa', 'KA-12-12332', 'Mysore')

rideService.offerRide('Shipra', 'Bangalore', 2, 'Polo', 'KA-05-41491', 'Mysore')

rideService.offerRide('Shashank', 'Hyderabad', 2, 'Baleno', 'TS-05-62395', 'Bangalore')

rideService.offerRide('Rahul', 'Hyderabad', 5, 'XUV',  'KA-05-1234', 'Bangalore')

rideService.offerRide('Rohan', 'Bangalore', 1, 'Swift', 'KA-01-12345', 'Pune')


# print(Ride.RIDES_DB)


rideService.selectRide('Nandini', 'Bangalore', 'Mysore', 1, 'Most Vacant')

rideService.selectRide('Gaurav', 'Bangalore', 'Mysore', 1, vehicleName='Activa')

rideService.selectRide('Shashank', 'Mumbai', 'Bangalore', 1, 'Most Vacant')

rideService.selectRide('Rohan', 'Hyderabad', 'Bangalore', 1, vehicleName='Baleno')

rideService.selectRide('Shashank', 'Hyderabad', 'Bangalore', 1,vehicleName='Polo')


# print(Ride.RIDES_DB)

rideService.endRide('Rohan', 'Hyderabad', 1, 'Swift', 'KA-01-12345', 'Bangalore')

rideService.endRide('Shipra', 'Bangalore', 1, 'Activa', 'KA-12-12332', 'Mysore')

rideService.endRide('Shipra', 'Bangalore', 2, 'Polo', 'KA-05-41491', 'Mysore')

rideService.endRide('Shashank', 'Hyderabad', 2, 'Baleno', 'TS-05-62395', 'Bangalore')




print(Ride.RIDES_DB)


rideService.printRideStats()