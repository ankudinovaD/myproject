"""
Рядки (Strings):
Напишіть функцію, яка приймає рядок і повертає його довжину.
Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
"""

#a

def len_str (user_string:str):
    return len(user_string)

#b

def str_concat (first_string:str, second_string:str):
    return first_string + ' ' + second_string

"""
Числа (Int/float):
Реалізуйте функцію, яка приймає число і повертає його квадрат.
Створіть функцію, яка приймає два числа і повертає їхню суму.
Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
"""

#c

def user_square (num):
    return num ** 2

#d

def add_num (first_num, second_num):
    return first_num + second_num

#e

def user_divmod (first_num:int, second_num:int):
    if second_num == 0:
        return "Помилка: ділення на нуль"
    return divmod(first_num, second_num)

"""
Списки (Lists):
Напишіть функцію для обчислення середнього значення списку чисел.
Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
"""

#f

def user_avg (user_list:list):
    if len(user_list) == 0:
        return 'Порожній список'
    return sum(user_list) / len(user_list)

#g

def common_elements(first_list:list, second_list:list):
    return list(set(first_list).intersection(second_list))

"""
Словники (Dictionaries):
Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
"""

#h

def get_key (user_dict:dict):
    return user_dict.keys()  

#print(get_key({"name": "Alexander", "lastname": "Tsin", "age": 36, "group": "PN121"}))

#i

def union_dict(first_dict:dict, second_dict:dict):
    return {**first_dict, **second_dict} # прийшлось гуглити :))

#print(union_dict({'a': 1, 'b': 2}, {'b': 99, 'c': 3}))

"""
Множини (Sets): 
Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
"""

#j
def common_set(first_set:set, second_set:set):
    return first_set.union(second_set)

#k

def is_subset(first_set:set, second_set:set):
    return first_set.issubset(second_set) # прийшлось гуглити :))

"""
Умовні вирази та цикли:
Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
"""

#l

def is_even(digit):
    """ Перевірка чи є парним число """
    return 'Парне' if digit % 2 == 0 else 'Непарне'

#m

def even_num(user_lst: list):
    return [num for num in user_lst if num % 2 == 0]