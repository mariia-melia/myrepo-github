array_of_strings = ['2,45,0', 'dfg%4,123,3', '38,76,999,1']

def sum_of_numbers_from_string(s):
    try:
        parts = s.split(",")  #ділення елементів по комах
        numbers = [int(x) for x in parts]  #перетворення елементів у числа
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

# для кожного елемента списку
for item in array_of_strings:
    print(sum_of_numbers_from_string(item))