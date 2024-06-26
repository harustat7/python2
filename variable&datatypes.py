"""
#for printing 
print("hello world") 
#here print acts as a function and is called the output

python character set
letters- A to Z, a to z
digits-0 to 9
special symbols-*,/,+,-
whitespaces-blank spaces,tab,newline etc
other charcters-python can process all the ASCII and unicode charcters as part of data or literals


print("Harustat is my name.","my age is 20 years")

#print numbers
print(10)

#print operations
print(23+34)


Variables
a variable is a name given to a memory location in a program
var=value

name="Harustat" #string(declare in double or single quotes)
age=24
print(name) #not print("name")
print(age)

print("my name is ",name)
print("my age is ",age)

# '=' assignment operator is stored in the left side datatype

age2 = age
print(age2)


rules for identifiers(names)
1) identifiers can be a combination of uppercase and lowercase letters,
digits or an underscore
so myVariable,variable_1,variable_for_orint all are python identifiers.
2)an identifier can not start with digit.so variable1 is valid but 1variable is not.
3)we can't use special symbols like !,@,#etc.
4)identifier can be of any length.
eg: thisismypythonvariable.(simple,short,meaningful ho-age,sum,count)

print(type(name))
print(type(age))


datatypes:
integers,strings,float,boolean,none

integers-> +ve,-ve,0 (int)
string-> "harustat",'hello','''niharika'''
float-> decimal values
boolean-> True or False (T and F are capital)
none->  a=none means no value is stored in that datatype currently

keywords
these are reserved words in python
ans,else,as,in,return,continye,true,while,break etc.

#python is case sensitive (eg: Apple and apple are different)

#print sum of two numbers
a = 2
b = 6
sum = a + b
print(sum)
diff=a-b
print(diff)


punctuators
these are symbols to organise sentence structure in programming language
(),{},@,[],+=,/=etc


#python is implicit typed language(datatype is automatically defined,no need to mention like in explicit typed language) 

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

input in python
input() statement is used to accept values from user using keyboard


#string input
name=input("name: ")
print(name)

#int input
age=int(input("age: "))

#float input
price=float(input("price: "))
print(price)


conditional statements
if-elif-else(SYNTAX)

if(condition):
Statement 1

elif(condition):
Statement 2

else:
StatementN 


#python is an identation language(mtlb jaise if ke baad colon lagana toh 4 spaces deni hai)

age=int(input("age: "))

if(age>=18):
    print("I can vote")

elif(age<18):
    print("cannot vote")

color=input("traffic light color: ")

if(color=="red"):
    print("stop")

elif(color=="yellow"):
    print("wait")

elif(color=="green"):
    print("go")

else:
    print("traffic light not working")


#single line if/ternary operator
<var>=<value>if<condition>else<var2>


food = input("food: ")
eat="yes" if food == "cake" else "no"
print(eat)

#<stt1> if<condition> else <stt2>
food=input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


#clever if/ternary statement
#<var>=(false_val,true_val)[<condition>]

age=int(input("age: "))
vote=("yes","no")[age<=18]

sal=float(input("salary: "))
tax=sal*(0.1,0.2)[sal>=50000]
print(tax)


#type of operators
an operator is a symbol that performs a certain oeration between operands
1)arithmetic operators(+,-,/,%,**)

2)relational/comparsion operators(==,!=,>,<,*=,%=,**=)

3)logical operators(not,and,or)

#arithemetic operators
a = 5
b = 3
print(a+b)
print(a-b)
print(a**b) #a^b
print(a/b)
print(a%b)#remainder


#relational operators
a=50
b=20

print(a == b)
print(a != b)
print(a < b)


#assignment operators
num=10
num=num+10
num+=10 #(line 240 and 241 have same meaning)
print(num)

num*=5
print(num)


#logical operators
print(not False)
print(not True)

a=50
b=30
print(not(a>b))

value1=True
value2=False

print(value1 and value2)
print(value1 or value2)


#type conversion
(one type of variable to another type)
it is of two types conversion(automatically) and casting(manually)


a=2 #if a is a string then it cannot be converted to float
b=4.25
sum=a+b #float is superior as compared to int
print(sum)

#type casting
a,b=2,"4.25"
c=float(b)
sum=a+c
print(sum)

a=3.14
a=str(a)
print(type(a))

#write a program to input 2 numbers and print their sum
num1=int(input("num1: "))
num2=int(input("num2: "))
sum=num1+num2
print(sum)

#wap to input the side of a square and print its area
side=float(input("side of square: "))
area=side*side
print(area)


#wap to input 2 floating point numbers and print their average
num1=float(input("num1: "))
num2=float(input("num2: "))
average=(num1+num2)/2
print(average)
"""

#wap to input 2 int numbers a and b
#print true if a is greater than or equal to b.if not then print false

n1=int(input("n1:"))
n2=int(input("n2:"))

if(n1>=n2):
    print("True")

else:
    print("False")