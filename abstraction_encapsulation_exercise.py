import sys

#class ==> carRental
#layers of abstraction ==> display cars and their cost, calculate and display fare
class carRental:
    
    def __init__(self, dictCars):
        self.dictCars = dictCars
    
    def displayCarsWithCost(self):
        for car in self.dictCars.keys():
            print("{} costs ${}/day".format(car, self.dictCars[car]))
        
    def calculateDisplayFare(self, car, days):
        if car in self.dictCars.keys():
            totalCost = days * self.dictCars[car]
            print("You would have to pay : ${}".format(totalCost))
        else:
            print("Sorry, the car you requested is not available")
    
    
    
#class ==> Customer
#layers of abstraction ==> car to borrow, number of days to Borrow the car for
class Customer:
    
    def carToBorrow(self):
        print("Please enter the name of the car you would like to borrow")
        self.car = input()
        return self.car
    
    def daysToBorrow(self):
        print("Please enter the number of days you would like to borrow", self.car)
        self.days = input()
        return int(self.days)
    
    
carrental = carRental({"Hatchback":30, "Sedan":50, "SUV":100}) 
customer = Customer()

while True:
    print("\n")
    print("Enter 1 to display the available cars and their cost")
    print("Enter 2 to select a car and the #days you would like to borrrow it for")
    print("Enter 3 to exit")

    userChoice = int(input())
    if userChoice == 1:
        carrental.displayCarsWithCost()
    elif userChoice == 2:
        car = customer.carToBorrow()
        days = customer.daysToBorrow()
        carrental.calculateDisplayFare(car, days)
    elif userChoice == 3:
        sys.exit(1)
    else:
        print("Please enter a valid choice!")
