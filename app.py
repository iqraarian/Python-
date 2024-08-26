                                #CASE SENSITIVE LANGUAGE
                                #PYTHON IS IMPLICIT LANGUAGE
# our first program
print("hello iqra")
print("My name is iqra. I'm 20 years old . And I'm still jobless ")
print(23+1)

#practise
name = "Iqra"
age = 19
price = 25.99
isactive = True
a = None

print(name)
print(age)
print(price)
print(isactive)
print(a)
print("This is my name:", name)

# Assignment operator
age2 = age
print("My age is :",age2)

#Datatypes
print(type(name))
print(type(age))
print(type(price))
print(type(isactive))
print(type(a))
 
 # example 1
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example 2
b=4
c=5
sum=b+c
print(sum)
print(type(sum))

#string "  " and numeric values can operate with *
# example 3
A,B=3,4
text="@"
print(2*text*4)

A,B=3,4
text="@"
print(A*text*B)

#example 4
A,B="3",4
text="@"
print((A+text)*4)

#example 5
C,D=5,7
E=6
print((C+D)*E)

#example 6
F,G=10,5.4
H=F*G
print(H)

#example 7
I,J=1,2
K=I/J
print(K)

#example 8
#integer Devision like answer is 0.5 L//M but integer devision round of answer 
# into small like 0.0
L,M=1.5,3
N=L//M
print(N,L/M)

#when the positive sign appear it moves to smallest one like ans is 2.4 but this move to 2
O,P=12,5
Q=O//P
print(Q)
#when the negative sign appear it moves to largest one like ans is -2.4 but this move to -3
R,S=-12,5
T=R//S
print(T)

#Example 9
#remainder is negative when denominator is negative 
#denominator is second value 
#whe denominator is nagative 2nd value
a,b=5,-2
c=a%b
print(c)
#when both are positive
a,b=5,2
c=a%b
print(c)
#when nominator is negtaive !st value
a,b=-5,2
c=a%b
print(c)
#when both are negative
a,b=-5,-2
c=a%b
print(C)