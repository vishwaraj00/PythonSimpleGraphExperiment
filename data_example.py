# data_example.py
# Reads file Qdata.txt. Calculates the average of the values in
# the 3rd column, including discharge data (m3/s) of river Tornionjoki, 
# on the border of Finland and Sweden. Finally the data is represented
# graphically. 

# Note: rows started with symbol # are comments - they are not executed
# by Python interpreter.

# At first additional Python modules are imported:
import sys
import numpy as np # short names like np are used to make code shorter
import matplotlib.pyplot as pp

# Let's open the file to variable dfile (it's just a name for 
# the variable, it can be 'x' or 'zxadawfpdq' as well)
dfile=open("Qdata.txt","r") 

sum=0
count=0
firstround=True
datalist=[]

for line in dfile :
# This is a loop. The following will be done for all lines.
# Note the indentation: in Python it's used to indicate which rows
# of the programming code are inside the block (in this case inside 
# the loop).
    if (firstround):
        firstround=False # the 1.row is a header, it's ignored
    else:
        fields=line.split()
        try:
# the first element in the list has index 0, the 3rd has index 2.
            value=float(fields[2]) # conversion from string to float, or real numbner
            sum=sum+value                   
            datalist.append(value)
            count=count+1
# Handling possible errors:
        except IndexError:
            continue
        except ValueError:      
            print("Error in the file.")
            sys.exit()

print("")
print("The average discharge on the whole period was ",sum/count)

pp.plot(datalist)
