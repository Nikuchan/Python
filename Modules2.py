#import Modules as mm
#from Modules import *
import sys
import random
import math
import datetime
import calendar
import os
sys.path.append('/home/sonicwall/Desktop')
from Modules import find_index,test

courses=['History','Math','Physics','  CompSci']

index=find_index(courses,'Math')
print("\n")
print(index)
print(test)

print(sys.path)

random_course= random.choice(courses)
print(random_course)

rads=math.radians(90)
print(rads)
print(math.sin(rads))

today=datetime.date.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())

print(os.__file__)