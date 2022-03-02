"""
When you add two very long numbers, you may face a memory overflow problem.
To avoid this problem, you can use BigInt.

However, BigInt is not supported in all browsers,
and sometimes the number is too big to be stored in BigInt.

To solve this problem, you can use string to store the number.

 1. When you receive two numbers, convert them to strings.

 2. From the all the way back of the strings, add them.

 3. Store the result in a variable. Let's say the name of the result as 'result'.

 4. The length of the result is maximally 2.
    Thus, If the length of the result is 2,
    store the first character of the result to another variable called "carry_sum".

 6. Repeat this process to the next digit.
    In this time, you need to calculate the sum of the second digits of the strings + the "carry_sum".

 7. If the length of calculation is 2,
    store the first character of the result to 'carry_sum' and the second character to 'result'.

 8. Repeat this process until there is no left characters for both strings.

 9. If there is a "carry_sum" left, add it to the end of the result.

10. Reverse the result, and return it.
"""


def add_big_numbers(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    carry_sum = 0
    result = ''

    # In the range of the length of each string, calculate the sum of the last digits.
    for i in range(max(len(num1), len(num2))):
        num1_digit = 0
        num2_digit = 0

        # If the length of the string is shorter than the index, add 0 to the string.
        if i < len(num1):
            num1_digit = int(num1[-i - 1])
        else:
            num1_digit = 0

        if i < len(num2):
            num2_digit = int(num2[-i - 1])
        else:
            num1_digit = 0

        # Calculate the sum of the last digits.
        sum_digit = num1_digit + num2_digit + carry_sum

        # If the sum is bigger than 9, add 1 to the carry_sum.
        if sum_digit > 9:
            carry_sum = 1
            sum_digit -= 10
        else:
            carry_sum = 0

        # Add the sum to the result.
        result += str(sum_digit)

    # If there is a carry_sum left, add it to the end of the result.
    if carry_sum > 0:
        result += str(carry_sum)

    # Reverse the result, and return it.
    print(int(result[::-1]))


add_big_numbers(123456789, 987654321)
