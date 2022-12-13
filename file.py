# Python program to create more then one directory easily

# importing os module
import os

# Directory Name
directory = "Lab "

# Parent Directory Path 
parent_dir = "D:/k"
i = 1
while i < 70: # No of folders to create
    path = os.path.join(parent_dir, directory+str(i))
    os.mkdir(path)
    i += 1
#Success Message
print("Directory '% s' created" % directory)