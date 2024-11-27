my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while my_list:
    num = my_list[0]

    if num >= 0:
        if num == 0:
            del num
        else:
            print(num)
        del my_list[0]
        continue
    elif  num < 0:
        break