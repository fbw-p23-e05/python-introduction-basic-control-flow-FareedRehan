# Task 1 - basic math operations

## Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.
## >Hint: you can use `for` or `while` loop to perform the same operation more than once!

### Option 1
number = 123
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
number = 32
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number") 

number = 121234
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

### Option 2
number = 123, 32, 121234
number = (int(input("Enter any number to test whether it is odd or even: ")))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
### :heavy_plus_sign: Task 2 - Calculate the sum of the numbers

## Your task is to write a program which asks the user three times for a number and prints the sum of those numbers.

### Option 1
number = 200
number = 500
number = 300
numbers = [200, 500, 300]
sum(numbers)
print("Sum of the numbers:", sum(numbers))
### Option 2
number1 = 200
number2 = 500
number3 = 300

number1 = int(input("number1: "))
number2 = int(input("number2: "))
number3 = int(input("number3: "))

sum = number1 + number2 + number3
print("Sum of the numbers: ", sum)

### :heavy_plus_sign: Task 3 - Find the maximum number

# Your task is to write a program which asks the user five times for a number and prints the maximum of those numbers.

number: 50
number: 680
number: 7
number: 1030
number: -4 
numbers = [50, 680, 7, 1030, -4]
Maximum = max(numbers)
print('Maximum of the numbers:', max(numbers))
### Option 2
number: 50
number: 680
number: 7
number: 1030
number: -4 
list = []
num = int(input("Enter number of elements in the list: ", ))
for i in range(5):
    ele = int(input("Enter numbers: "))
    list.append(ele)
    print("Maximum of the numbers:", max(list))
    
### :heavy_plus_sign: Task 4 - finding divisors of a number

# Your task is to write a program which prints all the divisors of a number. 
# The number comes from the user's input.
numb = 56
num = int(input("Enter an integer:" , ))
print("The divisor of the number are:", )
for i in range(2, num + 1):
    if(num % i == 0):
        print(i)

### :heavy_plus_sign: Task 5 - Check if a number is even and divisible by 3

#Your task is to write a program which asks the user for a number and prints if it is even and divisible by 3.

### Option 1
num = 6
num = int(input("Enter an integer:" , ))
if num % 2 == 0 and num % 3 == 0:
    print("6 is even and divisible by 3.")
### Option 2
num = 6
num = int(input("Enter an integer:" , ))
if num % 2 == 0:
    print("6 is even.")  
num = int(input("Enter the number whose divisibility needs to be checked: ", ))
div = int(input("Enter the number with which divisibility needs to be checked: ", ))
if num % div == 0:
    print("Divisible by 3.", )

### :heavy_plus_sign: Task 6 - Check if a number is positive, odd and divisible by 7

# Your task is to write a program which asks the user for a number and prints if a number is positive, odd and divisible by 7

### Option 1
num = 21
num = int(input("Enter an integer:" , ))
if num > 0 and num % 2 != 0 and num % 7 == 0:
    print("21 is positive, odd an divisible by 7.")
else: 
    print("21 is not positive, ot odd and not divisible by 7.")
### Option 2
num = 21
num = int(input("Enter an integer:" , ))
if num > 0:
    print("The number is positive.")
if num % 2 != 0:
    print("The number is odd.")  
num = int(input("Enter the number whose divisibility needs to be checked: ", ))
div = int(input("Enter the number with which divisibility needs to be checked: ", ))
if num % div == 0:
    print("The number is divisible by 7.", )
### Option 3
num = 21
num = int(input("Enter an integer:" , ))
if num < 0:
    print("21 is positive.")
elif num % 2 == 0:
    print("Even.")
elif num % 7 != 0:
    print("Divisible by 7.")
else:
     print("21 is positive, odd and divisible by 7.")