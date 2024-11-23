first_str = False
first = first_str #Без этой строчки 33 строка показывала "желтую" ошибку,
                  # Python не мог распознать переменные first и тд.
                  # программа работала, но ошибка напрягала
while not first_str:
    first = input('Введите первое число: ')
    if first.isdigit():
        first = int(first)
        first_str = True
    else:
        print('Что-то пошло не так')
# данные блоки позволяют без перезапуска изменить значение введенного значения, если ввели не целое число
second_str = False
second = second_str
while not second_str:
    second = input('Введите второе число: ')
    if second.isdigit():
        second = int(second)
        second_str = True
    else:
        print('Что-то пошло не так')

third_str = False
third = third_str
while not third_str:
    third = input('Введите третье число: ')
    if third.isdigit():
        third = int(third)
        third_str = True
    else:
        print('Что-то пошло не так')

if first == second == third:  # if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

# изначальное дз, сделанное ночью

#first = int(input('Введите первое число: '))
#second = int(input('Введите второе число: '))
#third = int(input('Введите третье число: '))

# if first == second == third:  #if first == second and first == third:
#     print(3)
# elif first == second or first == third or second == third:
#     print(2)
# else:
#     print(0)