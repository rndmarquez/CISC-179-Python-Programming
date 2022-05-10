"""
    File: vehicle.py
    Author: Ron Marquez

    File creates 2 different types of vehicles, Cars and Airplanes.
    Attributes for these vehicle can be recorded such as name, max_speed and number of engines or number of cylinders.
    File will also compare the 2 max speeds of vehicles and will print out vehicle with the max speed

    Vehicle = superclass
    Car = subclass to Vehilce
    Airplane = sublclass to Vehicle

"""

#define a class called Vehilce
class Vehicle(object):

    def getName(self):
        """
            returns name of self
        """
        return self.name
   
    def getMax_speed(self):
         """
            returns max_speed of self
         """
         return self.max_speed

    def setName(self, newName):
        """
            sets the name of set name given
        """
        self.name = newName

    def setMax_speed(self,newMaxSpeed):
        """
            sets the max_speed to speed given
        """
        self.max_speed = newMaxSpeed

    def __str__(self):
        """
            string function returns the name and max_speed of the vehickle
        """
        print("Name: " + self.name)
        print("Max Speed: "+ str(self.max_speed))
    
    def __init__(self, name,max_speed):
        """
            initialize with name and max_speed of varibles
        """
        self.name = name
        self.max_speed = max_speed


class Car(Vehicle):
    """
        Class for cars that is a subclass of class Vehicle
    """
    def getNumber_of_cylinders(self):
        """
            Return teh number of cylinders
        """
        return self.number_of_cylinders

    def setNumber_of_cylinders(self, newNumbers_of_cylinders):
        """
            Set the new number of cylinders
        """
        self.numbers_of_cylinders = newNumbers_of_cylinders

    def __str__(self):
        """
            string function that prints name, max_speed, and number ofcylinders
        """
        Vehicle.__str__(self)
        print("Number of clyinders: " + str(Car.getNumber_of_cylinders(self)))

    def __init__(self, name, max_speed, number_of_cylinders):
        """
            initalize Car class utilizing superclass Vehicle
        """
        self.number_of_cylinders = number_of_cylinders
        Vehicle.__init__(self, name, max_speed)
        
        
class Airplane(Vehicle):

    def __init__(self, name, max_speed, number_of_engines):
        Vehicle.__init__(self, name, max_speed)
        self.number_of_engines = number_of_engines

    def getNumber_of_engines(self):
        """
            return number of engines for the airplane
        """
        return self.number_of_engines

    def setNumber_of_engines(self, newNumber_of_engines):
        """
            set new number of engines for airplane
        """
        self.number_of_engines = newNumber_of_engines

    def __str__(self):
        Vehicle.__str__(self, name, max_speed, number_of_engines)
        print("Number of engines: " + str(Airplane.getNumber_of_cylinders(self)))
    


#define main function
def main():


    #create an instance of car class
    myCar = Car("honda", 100, 4)

    #create an instance of airplane class
    myAirplane = Airplane("Boeing", 800, 2)

    #call all get methods for Car
    print("Car name: " + Car.getName(myCar))
    print("Car Max Speed: " + str(Car.getMax_speed(myCar)) + " mph")
    print("Car number of cylinders : " +str(Car.getNumber_of_cylinders(myCar)))

    #call all get methods for Airplane
    print("Airplane name: " + Airplane.getName(myAirplane))
    print("Airplane max speed: " + str(Airplane.getMax_speed(myAirplane)) + " mph")
    print("Airplane number of engines: " + str(Airplane.getNumber_of_engines(myAirplane)))

    #increase speed of car by 50
    currentCarMaxSpeed = Car.getMax_speed(myCar)
    Car.setMax_speed(myCar, currentCarMaxSpeed + 50)
    print("New Car Max Speed: " + str(Car.getMax_speed(myCar)))

    #increase speed of airplane by 100
    currentAirplaneMaxSpeed = Car.getMax_speed(myAirplane)
    Car.setMax_speed(myAirplane, currentAirplaneMaxSpeed + 100)
    print("New Airplane Max Speed: " + str(Car.getMax_speed(myAirplane)))

    #comapre max_speed of airplane and car, print which is faster
    planeMaxSpeed = Airplane.getMax_speed(myAirplane)
    carMaxSpeed = Car.getMax_speed(myCar)


    if planeMaxSpeed > carMaxSpeed:
        print("Airplane speed, " + str(Airplane.getMax_speed(myAirplane)) + "mph, is greater than car speed, " + str(Car.getMax_speed(myCar)) + " mph")
    elif planeMaxSpeed < carMaxSpeed:
        print("Car speed, " + str(Car.getMax_speed(myACar)) + "mph, is greater than airplane speed, " + str(Airplane.getMax_speed(myAirplane)) + " mph")
    elif planeMaxSpeed == carMaxSpeed:
        print("Car max speed and Airplane max speed are equal at " + str(Airplane.getMax_speed(myAirplane)) + " mph")



    
if __name__ == "__main__":
    main()
