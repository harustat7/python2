#for printing 
print("hello world") 
#here print acts as a function and is called the output

"""python character set
letters- A to Z, a to z
digits-0 to 9
special symbols-*,/,+,-
whitespaces-blank spaces,tab,newline etc
other charcters-python can process all the ASCII and unicode charcters as part of data or literals
"""

print("Harustat is my name.","my age is 20 years")

#print numbers
print(10)

#print operations
print(23+34)

'''
Variables
a variable is a name given to a memory location in a program
var=value
'''
name="Harustat" #string(declare in double or single quotes)
age=24
print(name) #not print("name")
print(age)

print("my name is ",name)
print("my age is ",age)

# '=' assignment operator is stored in the left side datatype

age2 = age
print(age2)

"""
rules for identifiers(names)
1) identifiers can be a combination of uppercase and lowercase letters,
digits or an underscore
so myVariable,variable_1,variable_for_orint all are python identifiers.
2)an identifier can not start with digit.so variable1 is valid but 1variable is not.
3)we can't use special symbols like !,@,#etc.
4)identifier can be of any length.
eg: thisismypythonvariable.(simple,short,meaningful ho-age,sum,count)
"""

print(type(name))
print(type(age))

"""
datatypes:
integers,strings,float,boolean,none

integers-> +ve,-ve,0 (int)
string-> "harustat",'hello','''niharika'''
float-> decimal values
boolean-> True or False (T and F are capital)
none->  a=none means no value is stored in that datatype currently
"""