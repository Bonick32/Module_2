my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]


while True:
    num = my_list[0]
    quantity = len(my_list)

    if num >= 0 and quantity > 0:
        print(num)
        del my_list[0] # надеюсь не слишком радикально для этой задачи
        continue
    elif num < 0 or quantity == 0:
        break