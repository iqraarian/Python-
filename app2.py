#INPUT IN PYTHON
#input string
name=input("name: ")
print(name)
#input int
age=int(input("age: "))
print(age)
#input float
price=float(input("price: "))
print(price)
print("My name is",name,"I'm ",age,"years old")

#example 1
age=int(input("age: "))
if(age>=18):
    print("valid")
elif(age<=18):
    print("not valid")
else:
    print("not appllying please ")

#example 2

light=input("light color: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

#example 3
marks=int(input("marks: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

#example 4

A=int(input("A: "))
G=input("M/F: ")
if((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 and G=="M"):
    print("fee is 300")
else:
    print("no fee")

#ternary operator   SINGLE LINE IF
# example 5

food=input("food: ")
eat="yes" if food=="cake" else "no"
print(eat)

#example 6

food=input("food: ")
print("metha") if food== "cake" or food=="jalebi" else print("not metha")

#ternary operator CLEVER IF
#example 7

age=int(input("age: "))
vote=("no","yes")[age>=18]
print(vote)

#example 8
sal = float(input("salary: "))
tax=sal*(0.2,0.1)[sal>=50000]
print(tax)

