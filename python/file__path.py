import os

print os.getcwd()
print os.path.basename(__file__)
print os.path.abspath(__file__)
print os.path.dirname(__file__)
print os.path.dirname(os.path.abspath(__file__))
print(os.path.join(os.path.dirname(__file__))) 
