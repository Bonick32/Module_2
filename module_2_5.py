# пока искал способ выполнения ДЗ по необходимому условию, получился такой результат:

# def get_matrix_easy(n, m, value):
#     matrix = []
#     for i in range(n):
#         matrix.append([value] * m)
#     return matrix
#
# result1 = get_matrix_easy(2, 2, 10)
# print(result1)


# def get_matrix(n, m, value):
#     matrix = []
#     for i in range(n):
#         matrix.append([])
#         for j in range(m):
#             matrix[i].append(value)
#
#     return matrix


def get_matrix(n, m, value):
    return [[value for _ in range(m)] for _ in range(n)] #blackbox оптимизировал функцию...



result_1 = get_matrix(3,5,48)
result_2 = get_matrix(2, 2, 7890)
result_3 = get_matrix(5,3,0)
print(result_1)
print(result_2)
print(result_3)


