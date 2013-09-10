http://www.ibm.com/developerworks/library/l-pyint/index.html
help()
keywords
modules
introspection is the act of self-examination. Introspection refers to the examination of one's own thoughts, feelings, motivations, and actions. The great philosopher Socrates spent much of his life in self-examination, encouraging his fellow Athenians to do the same. He even claimed that, for him, "the unexamined life is not worth living.
 help('modules')
 help('modules keywords')
Python provides a way to examine the contents of modules (and other objects) using the built-in dir() function.

>>> __builtins__ is a attribute
<module '__builtin__' (built-in)>


So __builtins__ appears to be a name in the current scope that's bound to the module object named __builtin__. (Since modules are not simple objects with single values, Python displays information about the module inside angle brackets instead.)
import sys as s
s.modules.keys()
s.modules()#see the builtin modules
"Portable Operating System Interface", POSIX

Loosely speaking, computers can only execute programs written in low-level languages. Thus, programs written in a high-level language have to be processed before they can run. This extra processing takes some time, which is
a small disadvantage of high-level languages.

First, it is much easier to program in a high-level language. Programs written in a high-level language take less time
to write, they are shorter and easier to read, and they are more likely to be correct. Second, high-level languages are portable, meaning that they can  run on different kinds of computers with few or no modifications. Low-level
programs can run on only one kind of computer and have to be rewritten to run
on another. Due to these advantages, almost all programs are written in high-level languages.
Low-level languages are used only for a few specialized applications.

SOURCE
CODE  ------>INTERPRETER--->OUTPUT

A compiler reads the program and translates it completely before the program starts running.

the high-level program is called the source code,
and the translated program is called the object code or the executable. Once
a program is compiled, you can execute it repeatedly without further translation.
SOURCE
CODE  --->COMPILER--->OBJECT CODE--->EXECUTOR--->OUTPUT

Python is considered an interpreted language because Python programs are ex-
ecuted by an interpreter. There are two ways to use the interpreter: command-
line mode and script mode. In command-line mode, you type Python programs
and the interpreter prints the result:

A program is a sequence of instructions that specifies how to perform a com-putation. The computation might be something mathematical, such as solving a system of equations or finding the roots of a polynomial, but it can also be a
symbolic computation, such as searching and replacing text in a document or (strangely enough) compiling a program.

 we can describe programming as the process of breaking
a large, complex task into smaller and smaller subtasks until the subtasks are
simple enough to be performed with one of these basic instructions.

debugging?
Programming is a complex process, and because it is done by human beings,
it often leads to errors. For whimsical reasons, programming errors are called
bugs and the process of tracking them down and correcting them is called
debugging.
Three kinds of errors can occur in a program: syntax errors, runtime errors,and semantic[wrong] errors.

Programming languages are formal languages that have been designed to express computations.
algorithm: A general process for solving a category of problems

syntax: The structure of a program.


print 'process created'

while True:
    #next_line = proc.communicate()[0]
    next_line = proc.stdout.readline()
    if next_line == '' and proc.poll() != None:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

print 'done'


if should start with hierrachy.
if cond
    if: 
    print "Hello"
    elif:
    else
        if:
        elif:
        
elif:

else

loops while and for loop
oridinal - 1,2,3,
cardinal(oridinal - 1) 0,1,2


debugging purpose 

every if should have an else otherwise die fun should be there
nesting of if deep one is enough

Rules For Loops

    Use a while-loop only to loop forever, and that means probably never. This only applies to Python, other languages are different.
    Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.
    
Tips For Debugging

    Do not use a "debugger". A debugger is like doing a full-body scan on a sick person. You do not get any specific useful information, and you find a whole lot of information that doesn't help and is just confusing.
    The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.
    Make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little.

Homework

Now write a similar game to the one that I created in the last exercise. It can be any kind of game you want in the same flavor. Spend a week on it making it as interesting as possible. For extra credit, use lists, functions, and modules (remember those from Ex. 13?) as much as possible, and find as many new pieces of Python as you can to make the game work.

There is one catch though, write up your idea for the game first. Before you start coding you must write up a map for your game. Create the rooms, monsters, and traps that the player must go through on paper before you code.

Once you have your map, try to code it up. If you find problems with the map then adjust it and make the code match.

One final word of advice: Every programmer becomes paralyzed by irrational fear starting a new large project. They then use procrastination to avoid confronting this fear and end up not getting their program working or even started. I do this. Everyone does this. The best way to avoid this is to make a list of things you should do, and then do them one at a time.

Just start doing it, do a small version, make it bigger, keep a list of things to do, and do them.

Symbolic links are different from hard links. Hard links do not link paths on different volumes or file systems, whereas symbolic links may point to any file or directory irrespective of the volumes on which the link and target reside.
 ln -s target_path link_path

    
write function

def fun():
    print "hello"

we can also call nested function
a = input("Please Enter a number:")
if a>=4:
 print "number is greater",a
elif a>=2:
 print "number are equal",a
else:
 print "lablab"


import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

input() will take input as int:
raw_input() will take input as string
tuples are immutable
list are mutable

CPython id() is the actual memory address of the variable. If you want it in hex format, call hex() on it.

x = 5
print hex(id(x))

>>> a,b = 5,6
>>> print bytes(id(a))
142196064
>>> print bytes(id(b))
142196052
print ("Hello, " + "world!") #concatenation of the string.

dir(os.path)

for root, dirs, files in os.walk("/"):
    print root
    print dirs
    print files

total = len(sys.argv)
a = 5
a+= 1 or a-= 1
a -=0
core built in not require any import.
#
"""asd"""

import random
random.__file__

a = "Hello's"
a = 'Hello\'s'
string1 = "He turned to me and said, \"Hello there\""
string2 = 'He turned to me and said, "Hello there"'
help()
keywords
modules

But in Python, integers are immutable
a = 5
b = a ++ 5    # b is assigned 10
b = a +++ 5   # b is again assigned 10
b = a ++++ 5

keyword: A reserved word that is used by the compiler to parse a program.
composition: The ability to combine simple expressions and statements into
compound statements and expressions

You can use triple-quoted strings. When they're not a docstring (first thing in a class/function/module), they are ignored.

Guido van Rossum (creator of Python) approves.

'''
This is a multiline
comment
'''

comments will not affect the execution of program.
cmd line arguments.
fun a(parameters):
  pass
parameter: A name used inside a function to refer to the value passed as an
argument.
local variable: A variable defined inside a function. A local variable can only
be used inside its function.

Conditional and Operations:
you can check whether one number is divisible by another—if x % y is zero, then x is divisible by y.
7/3 yeild 2 as quotient 7%3 yeild 1 as reminder
boolean : 1 or 0
logical:and,or,not
condition:if
alternate condition:if else
chained condition:if elif else
comparison operator: == != > <
The return statement allows you to terminate the execution of a function before
you reach the end.
The process of a function calling itself is recursion, and such functions are said
to be recursive.
def rec():
  rec()
Notice that we removed the print statements we wrote in the previous step.
Code like that is called scaffolding because it is helpful for building the program
but is not part of the final product.

As you should expect by now, you can call one function from within another.
This ability is called composition.
caffolding: Code that is used during program development but is not part of
the final version.

The expression in brackets is called an index   [7].
slice
a="welcome to python,"
a[5:8]
a[:8] a[3:] a[:]

greeting = "Hello, world!"
greeting[0] = ’J’
print greeting
# ERROR!
Instead of producing the output Jello, world!, this code produces the runtime
error TypeError: object doesn’t support item assignment.
Strings are immutable, which means you can’t change an existing string. The
best you can do is create a new string that is a variation on the original:
greeting = "Hello, world!"
newGreeting = ’J’ + greeting[1:]
print newGreeting
The solution here is to concatenate a new first letter onto a slice of greeting.
This operation has no effect on the original string.

