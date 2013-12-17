class Parent():
    parentattrb = 100
    def __init__(self):
        print "Calling parent Constructor"
    def parentMethod(self):
        print "Calling the parent method"
    def setAttr(self,attr):
        Parent.parentattrb = attr
    def getAttr(self):
        print "Parent Attribute",Parent.parentattrb

class Child(Parent):
    def __init__(self):
        print "Calling child Constructor"

    def childMethod(self):
        print "Calling child method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

