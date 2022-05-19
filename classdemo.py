#classes are user defined blueprint or prototype
#sum,Multiplication,addition, constant
#methods, class variables, instance variables, contructor etc


class Calculator: #class
    num = 100 #class variables
    #default constructor

    def __init__(self,a,b): #constructor name should be __init__
        self.firstNumber = a
        self.secondNumber = b
        print("I am call automatically when object is created")

    def getData(self): #method
        print("I now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  #syntax to create objects in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4, 5)  #syntax to create objects in python
obj1.getData()
print(obj1.Summation())