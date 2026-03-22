#chapter 1 - VARIABLES
# print("curd rice")
my_name="Mayura"
# print(f"My name is {my_name}")
age=24
grit=99.99
# has_job=0
has_job=True
#print(f"Hi, my name is {my_name} and i am {age}. I have grit score of {grit} and {has_job}, i have a job")

# if has_job:
#     print(f"{my_name} is employed")
# else:
#     print(f"{my_name} is unemployed")    

#chapter 2 -typecasting: the process of converting a  variable from one data type to another
# print(type(age))
# print(type(grit))
# print(type(my_name))
# print(type(has_job))

# age=str(age)
# age+=1
# print(age)

# age=bool(age)
# print(age)

# full_name=""
# full_name=bool(full_name)
# print(full_name)

#chapter-3 : input()  taking input from user and return entered data as string
# user_name=input("what's your name?")
# age=int(input("what's your age:"))
# if(age<30):
#     age+=30-age
#     print(f"{user_name}, you'll be soon {age} years old")
# user_name+=" Rockstar"
# print(f"Welcome {user_name}!")


# length=float(input("Enter length of rectangle in meters:"))
# breadth=float(input("Enter breadth of rectangle in meters:"))
# area=length*breadth
# print(f"Area of rectangle is {area} sq.mt")

# item=input("What item would you like to buy?")
# price=int(input("what's the price?"))
# qty=int(input("how many would you like?"))
# total=price*qty
# print(f"you bought {qty} {item} and the total is Rs.{total}")

#madlibs game
# adjective1=input("Enter adjective1:")
# adjective2=input("Enter adjective2:")
# noun1=input("Enter noun1:")
# adverb1=input("Enter adverb2:")
# print(f"today i went to {adjective1} place")
# print(f"I saw a {adjective2} bike")
# print(f"I saw a person named {noun1} playing flute {adverb1}")

#chapter-4: arithmetic operator
# x=-3.1349
# y=round(x)
# z=abs(x)
# a=pow(z,z)
# print(y,z,a)

import math
# x=34.9123
# a=math.ceil(x)
# b=math.floor(x)
# c=math.sqrt(x)
# print(a,b,c,math.pi,math.e)

# radius=float(input("enter the radius of the circle:"))
# area=math.pi*pow(radius,2)
# print(f"Area of circle with radius {radius} meter is {area} m^2")

# a=float(input("Enter side a's length:"))
# b=float(input("Enter side b's length:"))
# c=math.sqrt(pow(a,2)+pow(b,2))
# print(f"hypotenuse of a right angled triangle with sides {a} meter and {b} meter is {c} meter")

# age=int(input("Enter your age:"))
# if(age==30):
#     print(f"you are 30")
# elif(age>30):
#     print(f"you are {age-30} years over 30")
# elif(age>25):
#     print("you'll soon be 30")
# else:
#     print("learn bro, still you are young")

# username=input("Enter your name:")
# if(username==""):
#     print("You didn't enter your name,please do it")
# else:
#     print(f"Welcome {username}")

#python calculator
# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))
# operator=input("enter an arithmetic operator:")
# if(operator=="+"):
#     result=num1+num2
# elif(operator=="-"):
#     result=num1-num2
# elif(operator=="*"):
#     result=num1*num2
# elif(operator=="/"):
#     result=num1/num2
# print(result)

#logical operator
# weather="sunny"
# temperature=30
# if(weather=="sunny" and temperature==26):
#     print("go for a walk")
# else:
#     print("stay at home")

#conditional expresssion
# x=10
# print("positive" if x>0 else "negative")

# fullname=input("enter your fullname:")
# result=fullname.find("a")
# print(f"space is at index:{result}")

#phone_number=input("Enter your phone number:")
# if(phone_number.isdigit() and len(phone_number)==10):
#     print("phone number saved!")
# else:
#     print("enter a valid phone number")
# phone_number=phone_number.replace("-","")
# print(phone_number)

# username=input("Enter your name:")
# if(len(username)<=12 and username.isalpha()):
#     print("your username is valid")
# elif(username.find(" ")==True):
#     print("username contains space.Invalid username")
# elif(username.isalpha()==False):
#     print("username has digits.invalid username")
# elif(len(username)>12):
#     print("username has more than 12 characters. Invalid username")

# username=input("Enter your username:")
# while username=="":
#     print("you didn't enter username")
#     username=input("Enter your username:")
# print(f"hello {username}!")

#compound interest
# final_amount=principal_amount*(pow(1+rate_of_interest/number_of_terms,number_of_terms*time))

#for loop
# for x in reversed(range(1,11,2)):
#     if(x==7):
#         continue
#     print(x)
# print("hello")
# import time
# my_time=int(input("Enter time in seconds:"))
# for i in range(my_time,0,-1):
#     seconds=i%60
#     minutes=(i//60)%60
#     hours=(i//3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("hello,time's up")


#nested-loops
# num=int(input("enter a number:"))
# for i in range(0,100):
#     j=i+1
#     if(i+j==num):
#         print(f"{i} and {j} make up to {num} which are consecutives in the range of 100")
# print("not found in range of 100")

#collections : single variable used to store multiple values
#list[] ordered,muttable,duplicates allowed
#tuple() ordered, muttable , duplicates  allowed, FASTER
#set{} unordered, immutable(but add/remove ok), duplicates not allowed

# fruits=['apple','banana','blueberry','watermelon','guava','apple']
# for fruit in (fruits):
#     print(fruit)

# print(fruits[3])
# print(dir(fruits))
# print("pineapple" in fruits)

#2D collection
# fruits=['apple','banana','pineapple']
# dairy_products=['milk','paneer']
# groceries=[fruits,dairy_products]
# print(groceries[1][1])
# for item in groceries:
#     print(item)

#dictionary : collection of {key:value} pairs, ordered,muttable,no duplicates

# capitals={"India":"New Delhi",
#           "USA":"Washington DC",
#           "Russia":"Moscow",
#           "germany":"berlin"}

# print(capitals.get("India"))
# #print(capitals[0])
# capitals.update({"japan":"tokyo"})
# if capitals.get("japan"):
#     print("exists")
# else:
#     print("doesn't exist")
# capitals.popitem()
# keys=capitals.keys()
# for key in keys:
#     print(key)

# items=capitals.items()
# for item in items:
#     print(item)

# index=0
# key,value=list(capitals.items())[index]
# print(key,value)


# #function() a block of reuseable code, use () after function name to invoke it
# def greeting(name,age):
#     print("hello")
#     print(f"how are you {name}")
#     print(f"hai,you are {age}")

# greeting("mayura",24) #argument sent here : mayura


# def calculate_age(age,name):
#     if(age<=25):
#         return (f"{name} learn bro, you are still young")
#     elif(age>25 and age<30):
#         return(f"{name} , you'll be 30 soon")
#     else:
#         return(f"{name} , you are already over 30")
    
# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# result=calculate_age(age,name)
# print(result)

# def add(n1,n2):
#     return n1+n2

#num1,num2=map(int,input("enter 2 numbers:").split())  
# NOTE: input gives string, so use split to get ["num1","num2"] apply int,but it expects single value, so use map(int,  ) ["num1","num2"] becomes [num1,num2]

#default arguments
# def total(price,discount=7.5):
#     dis= (price*discount)/100
#     return price-dis

# amt=int(input("enter the price:"))
# res=total(amt)
# print(f"total is:{res:.2f}")

#keyword arguments
# def greet(greetings,first_name,last_name):
#     print (f"{greetings}, welocme {first_name} {last_name}")
# res=greet(first_name="D I",greetings="hello",last_name="Mayura")

#arbitrary arguments
#*args - to accepts any number of non-keywords arguments(this packs them into a tuple and place it inside *args)
#**kwargs - to accept any number of keyword-arguments( this places them inside kwargs as dictionary)

# def sum(*args):
#     total=0
#     for arg in args:
#         total+=arg
#     print(total)
# sum(1,2,3,4)

# def address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# def address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# address(street="arcade mall",town="RR nagar",city="blr")

# name="D I Mayura"
# for char in name:
#     print(char, end="-")

#list comprehension
# doubles=[]
# for i in range(1,11):
#     doubles.append(i*2)
# print(doubles)

# doubles=[x*2 for x in range(1,11)]
# print(doubles)

#switch statement
# def day_of_week(day):
#     match day:
#         case 1:
#             return "monday"
#         case 2:
#             return "tuesday"
#         case 3:
#             return "wednesday"
#         case 4:
#             return "thursday"
#         case 5:
#             return "friday"
#         case 6:
#             return "saturday"
#         case 7:
#             return "sunday"
# print(day_of_week(3))

 #variable scope = where a variable is visible and invisible
 #scope resolution (LEGB) local > enclosed > global > built-in
# def fun1():
#     #x=1
#     def fun2():
#         #x=2
#         print(x)
#     fun2()

# x=3
# fun1()

#OOPS in python
# from car import Car

# car1=Car("Amaze","Blue","2026")
# car2=Car("tiago","grey","2026")
# print(car1.model,car1.colour,car1.year)
# print(car2.model,car2.colour,car2.year)
# car2.drive()

#class variable
# class Student:
#     batch=2024
#     num_of_students=0
#     def __init__(self,name):
#         self.name=name
#         Student.num_of_students+=1
        

# student1=Student("david")
# student2=Student("raman")
# print(student1.name,student1.batch)
# print(f"batch of {Student.batch} has {Student.num_of_students} students,namely:")
# print(student1.name)
# print(student2.name)
    
#inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True
#     def run(self):
#         print(f"{self.name} runs")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")
#     pass

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} meow")
#     pass

# dog1=Dog("scoobie")
# print(dog1.name)
# dog1.run()
# dog1.speak()

# cat1=Cat("melody")
# print(cat1.name,cat1.is_alive)
# cat1.run()
# cat1.speak()

#multiple inheritance  : inherit from multiple parent class
# class Animal:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("walks")

# class Birds:
#     def __init__(self):
#         pass

#     def fly(self):
#         print("flies")

# class Insects(Animal,Birds):
#     pass

# insect1=Insects()
# insect1.walk()
# insect1.fly()

#multilevel inheritance : inherit from a parent class which inherits from another class
# class Animal():
#     def __init__(self):
#         pass
#     def run(self):
#         print("runs")
# class Bird(Animal):
#     def __init__(self):
#         pass
#     def fly(self):
#         print("flies")
# class Insect(Bird):
#     pass
# insect1=Insect()
# insect1.run()
# insect1.fly()

#super() - allows to inherit methods of parent class to child class

#super() is used only when: we need to inherit constructor of parent class when child class has its own constructor as well.
#if child class doesn't have its own constructor , then we do not need super(), parent's constructor will be automatically inherited by child, also other parent class methods will also be inherited
# class Shape():
#     def __init__(self,color,is_filled):
#         self.color=color
#         self.is_filled=is_filled

# class Circle(Shape):
#     def __init__(self,radius,color,is_filled):
#         super().__init__(color,is_filled)
#         self.radius=radius

# class Rectangle(Shape):
#     def __init__(self,length, breadth,color,is_filled):
#         super().__init__(color,is_filled)
#         self.length=length
#         self.breadth=breadth

# circle=Circle(5,"blue",True)
# rectangle=Rectangle(4,5,"red",False)
# print(circle.radius,circle.color,circle.is_filled)
# print(rectangle.length,rectangle.breadth,rectangle.color,rectangle.is_filled)

#polymorphism (may forms)
#NOTE : ploymorphism using inheritance is common, but polymorphism done without using it is called ducktyping
# from abc import ABC,abstractmethod
# class Shape():
#     @abstractmethod   #abstract method - method declared in parent class without implementation, but msut be implemented in child class
#     def area():
#         pass

# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*(pow(self.radius,2))

# class Rectangle():
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth

# class Triangle():
#     def __init__(self,length,height):
#         self.length=length
#         self.height=height
#     def area(self):
#         return 0.5*self.length*self.height
    
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         self.topping=topping
#         super().__init__(radius)
    
# shapes=[Circle(3),Rectangle(3,4),Triangle(23,45),Pizza("sweet corn",5)]   #Pizza is a Shape, also a Circle, so this is polymorphism
# for shape in shapes:
#     print(f"{shape.area()}cm^2")

#Static method - a method that belongs to class rather than any object from that class(instance)

# class Employee:
#     def __init__(self,name, position):
#         self.name=name
#         self.position=position

#     def info(self):
#         print(f"{self.name} = {self.position}")

#     @staticmethod
#     def is_valid_position(position):
#         designations=["Manager","associate","team lead"]
#         return position in designations
           

# employee1=Employee("kumar","manager")
# employee1.info()
# print(Employee.is_valid_position("Manager"))

#class method : needs cls just like self, has access to class variable
# class Student:
#     count=0

#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         Student.count+=1

#     @classmethod
#     def count_students(cls):
#         return cls.count

# student1=Student("kiran","4.9")
# student2=Student("sharan","4.9")
# print(student1.name,student1.gpa)
# print(Student.count_students())

# @property - it lets us use method like an attribute
# reasons to use it: encapsulation(control access to data), validation, cleaner syntax
# getter,setter, deleter

# class Student:
#     def __init__(self,gpa):
#         self._gpa=gpa
#     @property
#     def gpa(self):
#         print(f"printing GPA:{self._gpa}")

#     @gpa.setter
#     def gpa(self,value):
#         print(f"setting GPA:{value}")
#         if value<0 or value>10:
#             print("invalid GPA")
#         else:
#             self._gpa=value
#     @gpa.deleter
#     def gpa(self):
#         print("deleting GPA")
#         del self._gpa

# student1=Student(4)
# student1.gpa
# student1.gpa=11
# student1.gpa
# del student1.gpa

#@decorators - a function that extends the behaviour of another function without modifying the base function
# a decorator always takes a function as input
# def add_sprinkler(func):
#     def wrapper():
#         print("added sprinklers!")
#         func()
#     return wrapper

# @add_sprinkler
# def get_icecream():
#     print("here's your icecream")

# get_icecream()

#multithreading = used to perform multiple taks concurrently(multitasking)
#syntax:    #threading.Thread(target=my_func)

# import threading
# import time

# def walk(name):
#     time.sleep(8)
#     print(f"walk {name}")
# def throw(name,adjective):
#     time.sleep(2)
#     print(f"{name},throw out trash {adjective}")
# def get():
#     time.sleep(4)
#     print("get mail")

# chore1=threading.Thread(target=walk, args=("blacky",)) #pass func reference not function() #to pass arguments, we neeed to sen it as tuple 
# chore2=threading.Thread(target=throw,args=("mike","immediately"))
# chore3=threading.Thread(target=get)

# chore1.start()
# chore2.start()
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("all chores done")


#how to connect to an APi in python
# import requests

# base_url="https://pokeapi.co/api/v2/"

# def get_info(name):
#     url=f"{base_url}/pokemon/{name}"
#     response=requests.get(url)
#     if(response.status_code==200):
#         poke_data=response.json()
#         return poke_data
#     else:
#         print(f"data could not be fetched {response.status_code}")

# name=input("Enter the pokeman name you want:")
# pokemon_info=get_info(name)
# print(f"name:{pokemon_info["name"]}")
# print(f"experience:{pokemon_info["base_experience"]}")
# print(f"held item:{pokemon_info["held_items"][0]["item"]["name"]}")


# "held_items": [
#   {
#     "item": {
#       "name": "metal-powder"
#     }
#   }
# ]

#  held_item is a list, so used index = held_item[0]
# then item is a dict, so used dict , key name =["item"]["name"]