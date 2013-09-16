#Keyword Arguments

def printme( str ):
    "This prints a passed string into this function"
    print str;
    return;

# Now you can call printme function
printme( str = "My string");

def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" );

#Default arguments:

# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( name="miki" );

#Variable-length arguments:
# Function definition is here
#An asterisk (*) is placed before the variable name that will hold the values of all nonkeyword variable arguments. This tuple remains empty if no additional #arguments are specified during the function call. Following is a simple example:
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 );
printinfo( 70, 60, 50 );
