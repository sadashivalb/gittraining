help()
keywords
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
