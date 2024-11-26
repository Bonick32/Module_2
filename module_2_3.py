my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]


while True:
    num = my_list[0]
    quantity = len(my_list)

    if num >= 0 and quantity > 1:
        if num == 0:
            del num
        else:
            print(num)
        del my_list[0] # надеюсь не слишком радикально для этой задачи
        continue
    elif  num < 0 or quantity == 1 :
        break

if my_list[0] > 0:
    print(my_list[0])   # оказывается, если quantity == 0, то выдает ошибку, когда список становится пустым, так как код
                        # обращается с просьбой вывести что-либо из пустого списка. данная строка - костыль для
                        # последнего элемента в списке