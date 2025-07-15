list_of_numbers = [-1, 2, 3, -4, 6, 7, 8, -11, 0, 10, 11, 9, 12, 14, 31, 16, 18, 17, 19, 20, -99]

sum_of_numbers = 0

for number in list_of_numbers:
    if number % 2 == 0:
        sum_of_numbers += number

print(sum_of_numbers)

