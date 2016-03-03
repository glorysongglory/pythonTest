'''
Created on 2016/3/3 16:29

@author: sodbvi
'''

import os		# Import the OS module
try:
    home = os.path.expanduser("D:/")          # Set the variable home by expanding the users set home directory
    print home                              # Print the location

    if not os.path.exists(home+'/testdir'):
        os.makedirs(home+'/testdir')        # If not create the directory, inside their home directory
except Exception as e:
    print e