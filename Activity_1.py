class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):

        #blind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelx = Vehicle(180, 23)

#access the variables inside init method
print("Model max speed:", modelx.max_speed)
print("Model mileage:", modelx.mileage)