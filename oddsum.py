def sum_odd_digits(number):
    odd_sum = 0
    number_str = str(number)
    for digit in number_str:
        digit = int(digit)
        if digit % 2 != 0:
            odd_sum += digit
    return odd_sum

number = int(input("Enter A Number: "))
result = sum_odd_digits(number)
print("Sum of odd digits:", result)
