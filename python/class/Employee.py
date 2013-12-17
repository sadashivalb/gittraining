class Employee():
    empcount = 0
    def __init__(self,name,salary):#__init__ is constructor
        self.name = name #self is paramter of every non static method
        self.salary = salary
        Employee.empcount += 1 #Access the class variable
    def displayCount(self):
        print "Total Employee:%d" %Employee.empcount

    def displayEmployee(self): #When your going to define method inside classs self will added as argument for
    #No need to call when you call methods
        print "Name:",self.name,"\nSalry:", self.salary

emp1 = Employee('sada',200)#emp1 is the object of class
emp2 = Employee('venkat',400)
emp1.age = 20
print emp1.age
del emp1.age
#print emp1.age
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print "Employee __doc__",Employee.__doc__
print "Employee __dict__",Employee.__dict__
print "Employee __module__",Employee.__module__
print "Employee __bases__",Employee.__bases__
print "Employee __name__",Employee.__name__
