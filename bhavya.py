# Trasfter statements
# 1. Break
# 2. Continue

# Functions:
# 1. Build in Functions
#     id()
#     print()
#     type()
#     input()
# 2. User defined Functions
#     def function_name(parameters):
#         "doc string"
#         ----
#         ----
#     return value
# parameters

# Retuning the values from  a function
# Types of arguments:

# 1. positional arguments
# 2. Keyword arguments:
# 3. Default argumetns:
# 4. Variable length arguments

# Functoins types
# 1. Recursive function:
# factorial of a number:
# 3! = 3*2*1
# 2. Lambda function:
#     anonymous function
# 3. Higher order Functions
# 4. Nested functions

# Function decorator:
# Generators:
# Modules:
# a grpup of functions, variables, and classes saved in a file
# every python file(.py) acts as a Module

# Special variable: __name__


# Packages: 
#     1. improve modularity
#     2. identity components uniquely
#     3. Naming conflicts


# __init__.py -  package declaration



# File Handling:
# Types of files:
#     1. Test files  : charecter data
#     2. Binary files: exectuable files, images, video files

# Opening a file:

# f=open(filename,mode)
# 1. read: poointer positied starting/beginning of the file
# 2. Write: override the data already present in the data
# 3. a(append): it will not override, pointer will point to last line
# 4. r+: read and write data, not override, file pointer is placed beginning
# 5. w+: write and read data. it override the exissint data
# 6.a+: to append and read data from file. It wont override exising data
# 7. x: exclustion crations, if file already there it will fileexistserror


# rb, wb, ab,--- binary modes

# Closing a file:
#     f.close()

# f=open("file1.txt",'w'):
# f.read()
# f.readable()
# f

# f.close()


# read()
# read(2) - 2 chars in the file
# readline() -  read line by line
# readlines()- read all lines and return in  a list


# the with statement:
# with open("filename","r") as f:
#     -----


# Exception Handling:
# 1. syntax errors: invalid syntax
# 2. Run time errors: due to invalid user input 

# Exceptions:
#     ex: Zerodevisions errors
#     typeerror
#     valueerror
#     filealreadyfounderror

#     Graceful termination of the program


# try:
#     read file from the remote location
# except FileNotFOunderror:
#     read file from the local workspace

# try:
#     Risky code
# except xxx:
#     Handlid excpetion/alternative code

# We generally can not use excetino handling to take care syntax errors

# finally block:

# try:
#     risky code
# except:
#     handinlg Exception
# finally:
#     cleanup the code


# Netmiko Library:
#     python library, that simlifies coneetging and automating network devices over ssh

# paramiko library: to connect to the devices and servers through ssh