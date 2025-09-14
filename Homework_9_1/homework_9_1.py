# функція-1 обчислює суму двох чисел
def sum_function(list_of_int):
    sum_of_digits = sum(list_of_int)
    print(f'result of addition action = {sum_of_digits}')
    return sum_of_digits

# функція-2 приймає список слів та повертає найдовше слово у списку
def return_longest_word (list_of_words):
    longest_word = max(list_of_words, key=len)
    print(f'Longest word is: {longest_word}')
    return longest_word

# функція-3 розрахує середнє арифметичне списку чисел
def arithmetic_mean(int_list):
    result = sum(int_list) / len(int_list)
    print (f'arithmetic mean = {result}')
    return result

# функція-4 "відфільтровує" некоректні символи в списку чисел
def sum_of_numbers_from_string(s):
    try:
        parts = s.split(",")  #ділення елементів по комах
        numbers = [int(x) for x in parts]  #перетворення елементів у числа
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

# функція-5 не пропускає 'h' and/or 'H'
def check_text_contains_h(text: str) -> str:
    if 'h' in text or 'H' in text:
        return "Текст містить h/H"
    else:
        return "Текст не містить h/H"