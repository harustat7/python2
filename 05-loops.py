"""
loops
loops are used to repeat instructions
they are of two types(while and for)
while condition:
    statement

count=1 #iterator
while count<=5: #iteration
    print("hello")
    count=count+1
    print(count)

i=1
while i<=5:
    print(i)
    i+=1

j=5
while j>=1:
    print(j)
    j-=1

#print the multiplication table of number n
i=1
n=int(input("num: "))
while i<=10:
    j=n*i;
    print(j)
    i+=1



#print the square of elements
i=1
while i<=10:
    j=i*i
    print(j)
    i+=1

#search for a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("x: "))
i=0
while i<len(tup):
    if(x==tup[i]):
        print("x found",x)
    else:
        print("x not found") 
    i+=1

break and continue:
break:used to terminate the loop when encountered

continue:terminates execution in the current iteration and continues execution of the loop with the next iteration
continue acts as skip

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1


for loops:
    for loops are generally used for sequential traversal.for traversing list,string.tuples etc.

nums=[1,2,3,4,5]
for val in nums:
    print(val)

tup=(3,6,8,9,10)
for val in tup:
    print(val)
else:
    print("end")


#search for a number x in the tuple using for loop
num=int(input("num: "))
arr=[2,5,7,8,10,34,56,78,46]
for val in arr:
    if(val==num):
        print("found",num)
        break
    
    else:
        print('not found')


#range
range  functions returns a sequence of numbers,starting from 0 by default,and increments by 1 by default and stops before the specified number
range(start?,stop,step?)

print(range(6))

seq=range(6)#ending number is not included
for i in seq:
    print(i)

for i in range(11):
    print(i)

for i in range(1,9,2):
    print(i)


#print the multiplication table of a number n
n=int(input("num: "))
for i in range(1,11):
    j=i*n
    print(j)

pass statement:
pass is a null statement that does nothing.it is used as a placeholder for future code.

for i in range(5):
    pass


#wap to find the sum of first n numbers(using while)
num=int(input("num: "))
i=0
sum=0
while i<=num:
    sum+=i
    i+=1

print(sum)
"""

#wap to find the factorial of first n numbers(using for)
num=int(input("num: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
 
print(factorial)