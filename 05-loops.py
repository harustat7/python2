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
"""
#print the multiplication table of number n
i=1
n=int(input("num: "))
while n<=10:
    j=n*i;
    print(j)
    i+=1


