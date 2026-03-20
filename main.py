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

username=input("Enter your username:")
while username=="":
    print("you didn't enter username")
    username=input("Enter your username:")
print(f"hello {username}!")
