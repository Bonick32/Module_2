numbers = list(range(1, 16))
# это сразу пришло на ум, увидев задание, ибо вручную набирать, как ниже - слишком длинно
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = list()
not_prime = list()

for i in numbers:
    if i > 1:
       for j in range(2, i):
           if i % j == 0:
               not_prime.append(i)
               break
       else:
           prime.append(i)

print("Prime", prime)
print("Not Prime", not_prime)

# почему else должен располагаться именно под for, а не как в приведенном ниже виде?
# я потратил 2 часа времени, пытаясь понять, почему написанный ниже код выводит несколько продублированных значений
# (несколько 7, 11, 13), пока на одном из сайтов не обратил внимание на расположение else не под if

# for i in numbers:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             print(i)
