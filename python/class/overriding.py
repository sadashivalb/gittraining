class Parent():
    def myMethod(self):
        print "Calling parent method"

class Child(Parent):
    def myMethod(self):
        print "Calling the Child method"

c = Child()
c.myMethod() #Child class overrides the method
#__init__ is constructor,obj = className(args)
#__del__ del obj,del obj

