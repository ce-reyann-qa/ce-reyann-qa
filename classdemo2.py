from classdemo import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = Child()
print(obj.getCompleteData())
