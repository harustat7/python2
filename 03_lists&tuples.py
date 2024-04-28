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

#tuples(a built-in data type that lets us create immutable sequencs of values.)
tup=(87,65,33,78,10)
print(tup[0])
tup1=()#empty tuple
print(tup1)
#slicing
print(tup[1:3])

#tuple methods

tup=(2,1,3,1)
print(tup.index(1))#returns index of first occurence
print(tup.count(2))#count total occurences

#wap to ask the user to enter names of their 3 favourite movies and stores them in a list.
n1=str(input("name of first movie:"))
n2=str(input("name of second movie:"))
n3=str(input("name of first movie:"))

list=[n1,n2,n3]
print(list)

#wap to check if list contains a palindrome of elements
list1=[1,'ab','ab',1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")
"""

#wap to count the number of students with grade A in the following tuple
tup=("c","d","a","a","b","b","a")

print(tup.count("a"))

#sort the above values in a list and sort them from "a" to "d"
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)
