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





