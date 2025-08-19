# Arm strong number in while loop

armstrong_number=int(input("Enter the number:"))
original_num=armstrong_number

total=0

while armstrong_number>0:

    digit=armstrong_number%10

    total=total+digit**3

    armstrong_number=armstrong_number//10

if total==original_num:
    print("an armstrong number")
else:
    print("not an armstrong number")


# armstrong number from range using functions

def my_function(armstrong_number):
    original_num=armstrong_number

    total=0

    while armstrong_number>0:

        digit=armstrong_number%10
        total=total+digit**3
        armstrong_number=armstrong_number//10

    return total==original_num
user_input_1=int(input("Enter the user_input_1:"))
user_input_2=int(input("Enter the user_input_2:"))

for i in range(user_input_1,user_input_2):
    if my_function(i):
        print(i)


#armstrong number any digits from user

def my_function(armstrong_number):
    original_num=armstrong_number

    total=0

    while armstrong_number>0:

        digit=armstrong_number%10
        total=total+digit**len(str(original_num))

        armstrong_number=armstrong_number//10

    return total==original_num

user_input_1=int(input("Enter the user_input_1:"))
user_input_2=int(input("Enter the user_input_2:"))
for i in range(user_input_1,user_input_2):

    if my_function(i):
        print(i)



# armstrong number in forloops and terbary operator

def my_armstrong_number(number):

    return sum(int(digit)**len(str(number)) for digit in str(number))==number

num=int(input("Enter the number:"))
if my_armstrong_number(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")


