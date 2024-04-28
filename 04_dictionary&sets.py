"""
#dictionary
dictionaries are used to store data values in key:value pairs
they are unordered,mutable(changeable) and don't allow duplicate keys

dict={
    "name":"harustat",
    "cgpa":7.40,
    "marks":[99,80,24],
    "age":20
}
print(dict)
#the keys cannot be lists and tuples
print(type(dict))
print(dict["cgpa"])
dict["surname"]="dua"
print(dict)

null_dict={
}
print(null_dict)

#nested dictionaries
student={
    "name":"harustat dua",
    "marks":{
        "english":59,
        "maths":100
    }
}
print(student)
print(student["marks"]["maths"])


#dictionary methods
print(student.keys())#return all the keys
print(student.values())#return all the values
print(student.items())#returns all(key,value)pairs as tuples
print(student.get("name"))#returns the key according to the value
student.update({"state":"punjab"})#inserts the specified items to the dictionary
print(student)


#sets
set is a collection of unordered items
each element in the set must be unique & immutable

nums={1,2,3,4}
set={1,2,2,2}
print(set)
#repeated elements stored only once,so it resolved to {1,2}
#null_set = set() #empty set
#in a set list and dictionary cannot be stored as they are mutable
#set is mutable(unhashable) but elements inside the set are immutable(hashable)

#set methods
set={1,2,3,4,5,2}
set.add(34)#adds an element
print(set)
set.remove(2)#removes an element
print(set)
#set.clear()#empties a set
print(set)
#set.pop()#removes a random value
print(set)

set2={4,5}
print(set.union(set2))#duplicate values are taken once
print(set2)
set.intersection(set2)
print(set2)


#wap to store following word meanings in apython dictionary:
table:"a piece of furniture","list of fact and figures"
cat:"a small animal"

dict={
    "table": ["a piece of furniture","list of fact and figures"],
    "cat": "a small animal"
}
print(dict)

#you are given a list of subject for students.assume that one classsroom is required for one subject.How many classrooms are needed by all students.
set={"python","java","c++","python","javascirpt","java","python","java","c++","c"}
print(set)
print(len(set))
"""
#wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & add one by one.use the subject name as key and marks as value.
dict={}
dict.update({"english":56})
dict.update({"maths":86})
dict.update({"hindi":90})
print(dict)

#figure out a way to store 9 and 9.0 as separate values in the set.(you can take help of built-in datatypes)
set={9,"9.0"}
print(set)