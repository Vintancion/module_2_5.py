def get_matrix(n, m ,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
              matrix[i].append(value)
        print(matrix)
    return(matrix)
n = int(input('размер строк :'))
m = int(input('размер столбцов :'))
value = input('значение :')
print('-------' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
                    print('матрица пуста:', n)
elif m <= 0:
                    print('матрца пуста:', m)
else:
                    print('матрица:')
for i in matrix:
                        print(*i)    

