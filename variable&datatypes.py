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
""""
keywords
these are reserved words in python
ans,else,as,in,return,continye,true,while,break etc.
"""
#python is case sensitive (eg: Apple and apple are different)

#print sum of two numbers
a = 2
b = 6
sum = a + b
print(sum)
diff=a-b
print(diff)

"""
punctuators
these are symbols to organise sentence structure in programming language
(),{},@,[],+=,/=etc
"""

#python is implicit typed language(datatype is automatically defined,no need to mention like in explicit typed language) 


"""
expression execution-
1) string and numeric values can operate together with *
a,b=2,3
txt="@"
print(2*txt*3)->so this expression @ is multiplied 6 times and shown as output @@@@@@

2)string and string can operate with +
a,b="12",3
txt="@"
print((a+txt)*b) ->12@12@12@
string and string can be joined with + symbol(concatenation)

3)numeric values can operate with all arithmetic operators
a,b=2,3
c=4
print(a+b*c)->14

4)arithmetic expression with integer and float will result in float
a,b=10,5.0
c=a*b
print(c)->50.0

5)result of division operator with two integers will be in float
a,b=1,2
c=a/b
print(c)->0.5

6)integer division with float and int will give int displayed as float
a=1.5,3
c=a//b
print(c,a/b)->0.0,0.5
integer division by rounding off to the smallest integer possible

floor gives the closest integer,which is lesser than or equal to the float value
result of(a//b) is same as the floor(a/b)
a,b=12,5
c=a//b
print(c)->2

a=-12,5
c=a//b
print(c)-> -3(smallest integer return krna -2.4)

7)reminder is negative if denominator is negative
a,b=5,-2
c=a%b
print(c)->-1
"""
