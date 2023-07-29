# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.


def my_pow(user_number: int, user_pow: int) -> int:
    if user_pow < 0:
        raise Exception('Enter only positive pow please!')
    if user_pow == 0:
        return 1
    if user_pow == 1:
        return user_number
    return user_number * my_pow(user_number, user_pow - 1)


try:
    user_number = int(input('Enter a number: '))
    user_pow = int(input('Enter a pow: '))
    print(my_pow(user_number, user_pow))
except Exception as error:
    print('Oops... some problem here, please try again')


# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)


###


# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.


###

