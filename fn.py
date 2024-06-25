
# if it is a multiply of 3 display of zip using range()

def check_multiple(number):
    if number % 3 == 0:
        return "Zip"
    else:
        return number

# Test the function with a range of numbers
for i in range(1, 21):
    print(check_multiple(i))
 

# if it is a multiply of 3 display of zip using input()
def check_multiple(number):
    if number % 3 == 0:
        return "Zip"
    else:
        return number

# Take input from the user
try:
    user_input = int(input("Enter a number: "))
    print(check_multiple(user_input))
except ValueError:
    print("Please enter a valid integer.")


# if it is a multiple of 5 display Zap
def check_multiple(number):
    if number %5==0:
        return "Zap"
    else:
        print("Invalid")

user_input=int(input("Enter a number: "))
print(check_multiple(user_input))


#if it is a multiple of both 3 and 5 display "Zoom"
def check_multiple(number):
    if number %5==0 and number %3==0:
        return "Zoom"
    else:
        return "Invalid"

user_input=int(input("Enter a number: "))
print(check_multiple(user_input))
