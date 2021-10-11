
#list can contain multiple types of data
a_list =['ip addresses', 30, 30]
print(type(a_list))

#print a single element from the list
print(a_list[1])

#change a value of one element from the list
a_list[1] = '100'
print(a_list[1])
print(len(a_list))

#append to a list
a_list.append(99)
print(len(a_list))

#add elemnets to a list:
a_list.extend([78, 23])
print(len(a_list))

#find entry in a list
print("100 is at index " ,a_list.index('100'))

#remove a specific entry in the list
a_list.remove('ip addresses')

#remove the last entry in a list
a_list.pop()
print(len(a_list))

#can also remove specific element from list
a_list.pop(0)
print(len(a_list))

### List slices
print("Now we look at list slices")
f =open("show_version.txt")
output = f.readlines()
print("The amount of lines in the list is" ,len(output) ,"and the type is" ,type(output) ,"\n")

#output lines 0 to 4
print(output[0:5])
# can ignore first number and just to
# [:5]
# or
# [:] will display all lines
# can also use minus numbers [-1:-5]
# this can be used to create a new list from another list
