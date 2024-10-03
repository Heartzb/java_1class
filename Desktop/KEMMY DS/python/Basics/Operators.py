# QUESTIONS
# 1. write a programe that takes two numbers as input and displays there sum, difference ,there product and there quotient
# 2.write a programe that converts two integers and prints whether the first integr is less than or equal to the second number
# 3.write a programe that checks if the given number is between ten and twenty and twenty inclusive using logical operators
# 4.write a programe that prints the squares of all integers from 1 to 10 using a four loop.
# write a simple program that prints if the user is above or equal to 18 you print adult and you are qualified if its less than 18 print not qualified9

# 5.we have the following details and marks enter these details from the key board
# student name = Ritah  Liz
#student number = SEP23/BCS/14
# programing = 78
#Data science = 89
#Computer Applications = 55
# calculate the average marks and print the answer in 3 decimal; places
# 6.write aprograme that converts celious temperature to feranerheight, the programe should displaythe converted temperature to feraneheight
# 7.A car's miles per gallaton can be calculated with the following formula
# 8.write a programe that asks a user for the number of miles driven and gallatons used it should calculate the car miles-per-gallons used and display the results
#MPG = miles Driven/ gallons of Gas used 


# OPERATORS These are used to performs on variables and values
# 1. Arithmatic operators eg, Additions + 
num1=4 
num2=8
sum=num1 + num2
 
 #Division
 # we use a /
 
 #3.Product
 # we use *
 
 # Modulus
 # it retuns the remainder of the numbers
 # 10%3=1
 
 # 4. Floor div //
 # it rounds off to the nearest number
 #9//2= 5


number_one=int(input("enter the first number one"))
number_two= int(input("enter the first number two"))
sum=number_one+number_two
print(f"The sum of {number_one} and {number_two}")
print("The sum is "+ str(sum))

product=number_one*number_two
print( f"The product of{number_one} and {number_two}")
print("The product is" + str(product))

Difference=number_one / number_two
print(f"The difference of {number_one} and {number_two}")
print("The difference is "+str(Difference))

modulus=number_one % number_two
print(f"The modulus of {number_one} and {number_two}")
print("The module is" + str(modulus))

quotient=number_one / number_two
print(f"The quotient  of {number_two} and {number_one}")
print("The quontient is" + str(quotient))

floordiv=number_one // number_two
print(f"The floor div of {number_one} and {number_two}")

# comparison
#greator than(>)(9>2)=true
#less than(<)(9<2)=false
#equal to (==)(9==2)=false
# not equal to (9!=2)=true

# if loops(commenting the comparision whether its true or false)
if number_one >number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_one} less than{number_two} ")
    





