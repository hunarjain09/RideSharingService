class Vehicle:
    VEHICLE_DB = {}
    def __init__(self,vehicleName,vehicleNumber):
        self.vehicleName = vehicleName
        self.vehicleNumber = vehicleNumber
        Vehicle.VEHICLE_DB[vehicleNumber] = self
        return
        