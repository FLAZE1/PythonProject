# print() выводит данные на экран
print("Hello world!") # двойные кавычки
print('Hello world') # одинарные кавычки
print(2026)

# короткий комментарий
''' длинный комментарий '''

# переменные
name = "Иван"
print("Воин", name)
print(f"Воин {name}")

num1 = 5
num2 = 10
total = num1 + num2
print(total)

num = 5
print(num)
num = 10
print(num)

num1, num2= 5, 6 #Множестввенное присваивание

# Правила наименования переменных
# Только латинские символы a-zA-Z
# Цифры можно использовать, но не на первой позиции
# Разрешен символ _
client1 = 1
client2 = 2
# 1car = 5 ошибка
# Нельзя использовать зарезервированные слова
# print = 10 нельзя

# snake_case - рекомендован
client_name = 'Иван'
ticket_price = 200

# camelCase
clientName = "Иван"
ticketPrice = 200

# Типы данных - у каждого своё предназначение
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))

# float / float / дробное число
my_float = 10.5
print(my_float, type(my_float))

# string / str / строка
my_str_1 = 'Hello1'
my_str_2 = "Hello2"
print(my_str_1, type(my_str_1))
my_str_3 = "Иван сказал: '...'"
print(my_str_3)
my_str_3 = 'Иван сказал: "..."'
print(my_str_3)

# boolean / bool / логический тип
my_bool_1 = True
print(my_bool_1, type(my_bool_1))
my_bool_2 = False
print(my_bool_2, type(my_bool_2))

# list / list / список - хранит упорядоченные значения
my_list = ["Иван", "Иван", 'Миша', 25]
print(my_list, type(my_list))

# tuple / tuple / кортеж - после создания нельзя изменить
my_tuple = (19, 'hello', 8.9)
print(my_tuple, type(my_tuple))

# set / set / множества - хранит только уникальные значения
my_set = {"Иван", "Иван", 'Миша', 25, 25 ,25}
print(my_set, type(my_set))

# dictionary / dict / словарь
my_dict = {'name': 'Егор', 'age': 15}
print(my_dict, type(my_dict))

# input() - считывает введенные значения
name = input('Введите имя:')
print(name, type(name))

# int() - переводит в целочисленный тип данных
num1 = int(15.5)
print(num1, type(num1))

# проблема с типами
num1 = int(input('Введите первое число:'))
num2 = input('Введите второе число:')
num2 = int(num2)
print(num1 + num2)
