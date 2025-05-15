# 1)
length = 5
width = 3
# Calculating area and perimeter of rectangle
area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


# 2)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Comparison
if a>b:
    print("First number is greater than second.")
elif a<b:
    print("First number is less than second.")
else:
    print("Both numbers are equal.")

#3)
year = int(input("Enter a year: "))
# Check Leap year 
if (year % 4==0 and year%100 !=0) or (year % 400 ==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#4)
# Arithmetic
print(10 + 5)
print(10 / 3)
print(10 // 3)
print(2 ** 3)
# Logical
print(True and False)
print(True or False)
print(not True)
# Assignment
x = 5
x += 2
print(x)

#5)
first_name = "sneha"
last_name = "choudhary"
# Concatenate with space
full_name = first_name + " " + last_name
print("Full Name:", full_name)

