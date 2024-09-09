# super class
class Vehicle:
    def __init__(mobile, vehicle_type):
        mobile.vehicle_type = vehicle_type


# child class
class Automobile(Vehicle):
    def __init__(mobile, vehicle_type, year, make, model, doors, roof):
        # use types for constructing child class data
        Vehicle.__init__(mobile, vehicle_type)
        mobile.year = year
        mobile.make = make
        mobile.model = model
        mobile.doors = doors
        mobile.roof = roof

    # returning data defined by a tab break
    def __str__(mobile):
        return "Vehicle type: " + mobile.vehicle_type + "\nYear: " + mobile.year + "\nMake: " + mobile.make + "\nModel: " + mobile.model + "\nNumber of doors: " + mobile.doors + "\nType of roof: " + mobile.roof


if __name__ == "__main__":
    # need inputs to add information
    year = input("Enter Car Year: ")
    make = input("Enter Car Make: ")
    model = input("Enter Car Model: ")
    doors = input("Enter Number of Car Doors: ")
    roof = input("Enter Car Roof: ")
    # object for car
    carObject = Automobile(year, make, model, doors, roof)
    print("Entered details are =>")
    print(carObject)