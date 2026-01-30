
# f=open("file1.txt",'w')
# print("file name", f.name)
# print("file name", f.mode)
# print("Is fiele is readbale", f.readable())
# print("Is file writable", f.writable())
# f.write("This is override data")
# print("is file is closed",f.closed)
# f.close()
# print("is file is closed",f.closed)




# f=open("file1.txt", 'r')
# # list=["athadu\n", "khaleja\n", "pokiri\n", "murari\n"]
# # f.writelines(list)
# data=f.readlines()
# for line in data:
#     print(line, end='')
# # print("List of lines written to the file successfully")

# f.close()

# with open("file1.txt", "w") as f:
#     f.write("Mahesh\n")
#     f.write("Nenokkadine\n")
#     f.write("bharth ane nenu\n")
#     print("Is file closed", f.closed)
# print("Is file closed", f.closed)

try:
    x=10
    print("this is from the try blcok",x/0)

except TypeError:
    print("this is from type error block, please check the value you passed")
except:
    print("there is some issue while execting the code")
finally:
    print("FINALLY")



# print(10/"ten")

