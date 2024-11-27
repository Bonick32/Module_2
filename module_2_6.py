import random
def stone_with_number():
    nums = list(range(3,21))
    sWn = random.choice(nums)
    return sWn
sWn = stone_with_number()

print(sWn)
num = 12
for i in range(1, 21):
    for j in range(1, 21):
        if sWn % (i + j) == 0:
            if i < j:
                print(f'{i}{j}', end = '')