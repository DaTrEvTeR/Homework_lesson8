# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.


# def my_pow(user_number: int, user_pow: int) -> int: # Створюємо функцію яка приймає число користувача та його сутпінь
#     if user_pow < 0: # Робимо перевірки на некоректний ввод користувача
#         raise Exception('Enter only positive pow please!')
#     if user_pow == 0:
#         return 1
#     if user_pow == 1:
#         return user_number
#     return user_number * my_pow(user_number, user_pow - 1) # Створюємо рекурсію та виводимо результат з функції
#
#
# try: # Обробляємо винятки та запитуємо в користувача число та ступінь для возведення
#     user_number = int(input('Enter a number: '))
#     user_pow = int(input('Enter a pow: '))
#     print(my_pow(user_number, user_pow))
# except Exception as error:
#     print('Oops... some problem here, please try again')


# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)


# def print_stars(count_of_stars: int) -> None: # Функція приймає к-сть зірок від користувача, та не повертає будь які значення
#     if count_of_stars < 1: # Робимо перевірку на некоректне введення користувача
#         raise Exception('Enter only positive integer number')
#     print('*', end=' ') # Виводимо зірку в консоль
#     if count_of_stars > 1: # Якщо користувач ввів більше чим 1 запускаємо рекурсію
#         print_stars(count_of_stars - 1)
#         # Рекурсія зменьшую к-сть введену користувачем з кожним разом виводячи зірку,
#         # поки змінна count_of_stars не = 1
#
#
# try:
#     user_count_of_stars = int(input('Enter count of stars: ')) # Запрошуємо в користувача ввести к-сть зірок
#     print_stars(user_count_of_stars) # Визиваємо нашу функцію
# except Exception as e:
#     print(e)

# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.


