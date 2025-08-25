# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from Homework_6_4.homework_6_4 import list_of_numbers


def multiplication_table(number):
    print(number)
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result: int = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_function(d, g):
    addition_action = int(d) + int(g)
    print('result of addition action: ' + str(d) + ' + ' + str(g) + ' = ' + str(addition_action))

sum_function(5, 4)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers_entered_by_user = [5, 7, 8, 16]

def arithmetic_mean(int_list):
    result = sum(int_list) / len(int_list)
    print (f'arithmetic mean = {result}')
    return result

arithmetic_mean(numbers_entered_by_user)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
entered_text = 'Kyiv is a capital of Ukraine'
reversed_text = ''.join(reversed(entered_text))
print(reversed_text)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list_of_fruits = ['apple', 'onion', 'watermelon']

def return_longest_word (list_of_words):
    longest_word = max(list_of_words, key=len)  # знаходимо слово з найбільшою довжиною
    print(f'Longest word is: {longest_word}')

return_longest_word(list_of_fruits)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 (from task 3: Написати функцію, яка розрахує середнє арифметичне списку чисел)
count_all_numbers = int(input("Введіть кількість чисел, які ви хочете ввести: "))
numbers_entered_by_user = []

for i in range(count_all_numbers):
    num = int(input(f"Введіть число №{i + 1}: "))
    numbers_entered_by_user.append(num)

def arithmetic_mean(int_list):
    result = sum(int_list) / len(int_list)
    print (f'arithmetic mean = {result}')
    return result

arithmetic_mean(numbers_entered_by_user)

# task 8 (from # task 5: Написати функцію, яка приймає список слів та повертає найдовше слово у списку)
words_entered_by_user = str(input("Введіть текст: "))

def return_longest_word (entered_text):
    words = entered_text.split()  # розбиваємо на слова
    longest_word = max(words, key=len)  # знаходимо слово з найбільшою довжиною
    print(f'Longest word is: {longest_word}')

return_longest_word(words_entered_by_user)

# task 9 (from # task 2: Написати функцію, яка обчислює суму двох чисел)
enter_numbers = int(input("Введіть кількість чисел, суму яких ви хочете знайти: "))
numbers_storage = []

for i in range(enter_numbers):
    num = int(input(f"Введіть число №{i + 1}: "))
    numbers_storage.append(num)

def sum_function(list_of_int):
    result_of_sum = sum(list_of_int)
    print(f'result of addition action = {result_of_sum}')
    return result_of_sum

sum_function (numbers_storage)

# task 10 (from task 4: Написати функцію, яка приймає рядок та повертає його у зворотному порядку)
get_string_from_user = str (input('Введіть текст: '))
reversed_text = ''.join(reversed(get_string_from_user))
print(reversed_text)