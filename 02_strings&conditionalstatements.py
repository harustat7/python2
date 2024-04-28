
#strings-strings is a type of datatype that stores the sequence of characters
#str1="this is a string"
#str2='this is a string'
#str3=this is a string"""

#if we use single quotes in a string then python will be confused 
#'this is apnacollege's tutorial'
#"this is apnacollege's tutorial"

#str4="this is a string.we are learing strings in python"

#escape sequence characters-\n(newline)

#str5="this is a string.\n we are learning strings"
#print(str5)

"""
#basic operations
#concatenation

str1="apna"
str2="college"
print(str1+" "+str2)


#length of string
str="hello"
len1=len(str)
print(len1)

#indexing
0 1 2 3 4 5 6 7 8 9 10 11
A p n a _ C o l l e g  e

str = "Apna_College"
ch=str[0]
print(ch)
#we can access the charcters of a string but cannot manupliate them.

#slicing
accessing parts of a string

str="ApnaCollege"
print(str[1:4])
print(str[ : 5])#[0:4]
print(str[2: ])#[2:len(str)]

#slicing for negative index
(backward counting)
a  p  p  l  e
-5 -4 -3 -2 -1

str="apple"
print(str[-3:-1])


#string functions
str="i am a coder"
print(str.endswith("er"))#return true if string ends with substring
print(str.capitalize())#captialise the first alphabet of the string
print(str.replace("o","a"))#replaces substring or particular alphabets from old character to new character
print(str.find("am"))#returns index where first the word or character is found
print(str.count("a"))#number of times the word or alphabet exists

#wap to input user's first name and print its length

name=str(input("name: "))
print(len(name))

#wap to find the occurence of '$' in a string
string="2$5$"
print(string.count("$"))


#nesting(if elif else statements)
age=99
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")

else:
    print("cannot drive")


#wap to check if a number entered by the user is even or odd
num=int(input("num: "))

if(num%2==0):
    print("number is even")

else:
    print("number is odd")


#wap to find the greatest of 3 numbers enetered by the user
num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))

if(num1>num2):
    if(num1>num3):
        print("num1 is the greatest",num1)

if(num2>num1):
    if(num2>num3):
        print("num2 is the greatest",num2)

if(num3>num1):
    if(num3>num2):
        print("num3 is the greatest",num3)
"""

#wap to check if a number is multiple of 7 or not
num=int(input("enter the num: "))
if(num%7==0):
    print("multiple of 7")
else:
    print("it is not the multiple of 7")