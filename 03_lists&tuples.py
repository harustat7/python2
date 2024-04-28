"""
#lists
a built-in datatype that stores set of values
it can stores elements of different types(integer,float,string etc.)


marks= [12,67,33,89,56.5,89.9]
print(marks)
print(type(marks))
print(marks[1])
print(len(marks))

student=["Harustat",24,"17-10-2003","Ludhiana"]
print(student)

#strings are immutable(cannot be changed) in python but lists are mutable(change)in python
str="hello"
#str[0]="b"
print(str)

student=["Harustat",24,"17-10-2003","Ludhiana"]
student[0]="Arjuna"
print(student)
#list slicing
list_name[starting index:ending index]

marks=[23,56,78,90,10]
print(marks[1:4])
print(marks[ :4])
print(marks[1: ])
print(marks[-3:-1])

#list methods

list=[2,1,3]
print(list)
list.append(4)#adds one lement at the end
print(list)
list.sort()#sorts in ascending order
print(list)
list.sort(reverse=True)#sorts in descending order
print(list)
list.reverse()#reverses list
print(list)
list.insert(2,10)#insert element at index (list.insert(idx,el))
print(list)
list.remove(1)#removes first occurence of the element
print(list)
list.pop(2)#pops the value at a specific index (list.pop(idx))
print(list)
"""