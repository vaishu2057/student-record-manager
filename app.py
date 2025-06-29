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

#LISTS....
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
fruits = [banana, apple, grapes]
fruits.sort
print(fruits)