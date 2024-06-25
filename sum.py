#Write a Python program to find the sum of digits of a given number.

#Example: Sum of digits of the number 123 will be 6

#Note: Initialize the number with various values and test your program.



def sum_of_digits(number):
    # Ensure the number is positive for digit sum calculation
    number = abs(number)
    digit_sum = 0
    
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum

# Test cases
test_numbers = [123, 456, 789, 0, -987]

for num in test_numbers:
    print(f"Sum of digits of {num} is {sum_of_digits(num)}")
