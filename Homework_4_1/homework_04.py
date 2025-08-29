adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace('\n', ' ')

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace('....', ' ')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
while "  " in adventures_of_tom_sawer:
    adventures_of_tom_sawer = adventures_of_tom_sawer.replace('  ', ' ')

# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""
print(adventures_of_tom_sawer.count('h'))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adventures_of_tom_sawer.split()          # розбиваємо текст по пробілах
count_capitalized = sum(1 for word in words if word[0].isupper())
print(count_capitalized)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
words = adventures_of_tom_sawer.split()
word_to_find = "Tom"

if words.count(word_to_find) >= 2:
    first_one = words.index(word_to_find)
    second_one = words.index(word_to_find, first_one + 1)  # шукаємо далі
    print(f"Вдруге слово '{word_to_find}' зустрічається на позиції:", second_one + 1)
else:
    print("No such word")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.replace('. ', '.\n')
print (adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
import re
sentences = re.findall(r'[A-Z][^\.]*\.', adventures_of_tom_sawer_sentences)

lower_4th_sentence = sentences[3].lower()

print ('4-те речення із малими літерами:', lower_4th_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for s in sentences:
    if s.startswith("By the time"):
        print("Знайдено речення:", s)

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
last_sentence = sentences[-1]   #останнє речення
words_in_last = last_sentence.split()
print("Кількість слів у останньому реченні:", len(words_in_last))