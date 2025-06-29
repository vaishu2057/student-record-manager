print("Hello World")
#'''print is function that gives the ouput . 
 #it prints the text present inside the paranthesis.
 #the text present inside the quotations is called STRINGS'''
print("hello world", "hi") 
#if we put a comma btw two strings they will print in ine line 


#VARIABLE : A variable is  a name given to a memory location in a program.. 
a = 23 + 44 -5
print(a)
name = 'pranu'
age = 18
print(name)
print(age)
print("my name is", name)
print("my age is", age)
"""variables cannot start from a digit.
 variable_3 is valid but 3variable is not valid"""


#PRACTICE.....
#write a program to input 2 numbers and print their sum
num1 = int(input("num1:"))
num2 = int(input("num2:"))
sum = num1 + num2 
print("sum =",sum)

#write a program to input side of a square and print its area..
side = int(input("side:"))
area = side * side
print('area of a square =',area)

#WAP to input 2 floating point numbers and print their average
a =  float(input("a:"))
b =  float(input("b:"))
avg = (a + b)/2
print("avg",avg)

#WAP to input 2 int numbers , a and b.Print True if a is greater than or equal to b. If not print False
a = int(input("a:"))
b = int(input("b:"))
if a>= b :
    print("True")
else :
    print("False")

# STRINGS....
'''string is a data type that stores a sequence of characters'''
# in strings \n is used tp print the line in next line and for tab space btw the strings we use \t
'''for example.. '''
str1 = "This is a string. \n We are creating it in python"
print(str1)
 
 #SOME FUNCTIONS....
str = " i am learning python"
print(str.endswith('on'))

str = "i am learning python"
print(str.replace("python","java"))

str = "i am learning python"
print(str.find("i"))

str = "i am learning python"
print(str.count("i"))

str = "i am learning python"
print(str.capitalize())

#IF-ELSE STATEMENTS....PRACTICE
#TASK -1 WAP to check if a number entered by the user is odd or even
a = int(input("a:"))
if a % 2 == 0 :
    print("the number is even ")
else:
    print("the number is odd")

#TAS-2 WAP to find the greatest of 3 numbers entered by the user
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a > b  and a > c :
    print(f"the greatest number is: {a}")
elif b > a and b > c :
    print(f"the greatest number is :{b}")
else :
    print(f"the greatest number is: {c}")
#TASK-3 WAP to check if a number is a multiple if 7 or not
a = int(input("a: "))
if a % 7 == 0 :
    print("the number is divisible by 7")
else:
    print("the number is not divisible by 7")

#LISTS....[lists are mutable data type whereas strings and tuples are immutable data type]
student = ["pranavi", 17 , "vizag"]
print(student)
print(student[0])
student[2] = 27
print(student)
print(student[-3])
print(len(student))
# SOME FUNCTIONS
student = ["pranavi", 17 , "vizag"]
student.append(6)
print(student)#append func add value in the list

stu = [2, 3, 4, 8]
stu.append(6)
stu.sort()#it will arrange the values inside the list in ascending order
stu.sort(reverse = True)# it will arrange in descending order
print(stu)

fruits = ['banana', 'apple','grapes' ]
fruits.sort()
print(fruits)

list = [2, 3, 6, 7]
list.reverse()#reverses the order of the values inside the list
print(list)

list = [2, 3, 6, 7]
list.insert(1, 9)#inserts the valuein that index
print(list)

list = [2, 3, 9,8, 9, 9, 7]
list.remove(9)#removes the first occurrence of element
print(list)

list = [2, 3, 9, 8, 9, 9, 7]
list.pop(4)#removes element at that index
print(list)
#TUPLE METHODS...
tup = (1,3,4,3,7)
print(tup.index(3))#returns index of first occurence
print(tup.count(3))#counts how many times the element occurs

#PRACTICE....
#WAP to ask the user to enter names of their 3 fav movies and store them in a list
movie1 = input("movie1:")
movie2 = input("movie2: ")
movie3 = input("movie3: ")
list = [movie1 , movie2, movie3]
print("list =", list)

#WAP to check if a list contains a palindrome of elements.(hint:use copy() method ) 
ist = [1 , 2, 3, 2, 1]
copy_list = list.copy()
copy_list.reverse()
if copy_list==list :
    print("palindrome")
else:
    print("not a palindrome")

#WAP to count the number of students with the "A" grade in the following tuple
tup = ["C","D", "A", "A", "B", "B", "A"]
print(tup.count("A"))

#Store the above values in a list & sort them from "A" TO "D"
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)

# DICTIONARY SETS.....
#dictionaries are used tp store data values in key:value pairs 
dict = { 
    "key" : "values",
    "name": "pranu",
    "age" : 17
}
print(dict)
#in dictionary, values can store all the data types but in key except list all the data types can be stored

#nested dictionary
student ={
    "name": "ravi",
    "subjects": {
        "phy": 98,
        "chem": 99,
        'maths': 92
    }
}

print(student)
print(student["subjects"])

#Dictionary methods...
print(student.keys())#returns all keys

print(student.values())#returns all values 

print(student.items())#returns all (key,val) pairs as tuples

print(student.get("name"))#returns the key according to value

student.update({"city":"vizag"})# inserts the specified items to the dictionary
print(student)

#SETS..they are mutable but elements of a set are immutable and repeated element is not count in a set.
#it does not contain lists , dictionary
collection = {1,2,3 ,3,3 ,3,4,"helloo world"}
print(len(collection))

#SETS methods ....
set = {1,2,3,4,}
set.add(24)#adds an element
print(set)

set.remove(2)#removes the element 
print(set)

set.clear()#empties the set
print(set)

set = {"hello","world","beauty"}
print(set.pop())

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))#combines both set values and returns new

print(set1.intersection(set2))#combines common values and returns new

#PRACTICE....
#task 1
#STORE following word meanings in a python dictionary:
'''table: "a piece of furniture ", "list of facts and figures"
    cat : "a small animal" '''
dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print(dict)

#task 2 
'''you are given a list of subjects for students.Assume one classroom is required
 for 1 subject . how many classrooms are needed by all students 
 "python", "java","C++","python","javascript","java","python","java","C++","C"
'''
subjects = {"python", "java","C++","python","javascript","java","python","java","C++","C"}
print(subjects)
print(len(subjects))#5 classrooms are required

#task 3 
'''WAP to enter marks of 3 subjects from the user and store them in a 
dictionary . start with an empty dict & add one by one . use subject name as key & marks as values '''
marks = {}

a = int(input("enter phy: "))
marks.update({"phy": a})

b = int(input("enter chem: "))
marks.update({"chem": a})

c = int(input("enter maths: "))
marks.update({"maths": a})
print(marks)

#task 4 
'''figure out a way to store 9 & 9.0 as seperate values in the set
(you can take help of built-in data types)'''
numbers = {9,'9.0'}
print(numbers)
#OR
numbers ={
    ("float",9.0),("int",9)
    }
print(numbers)
