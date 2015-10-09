__author__ = 'girish'
def weighted_edit_distance(word1,word2,constraint):
    insert,delete,replace = constraint
    i = len(word1)
    j = len(word2)

    matrix = [[0 for _ in range(j)] for _ in range(i)]

    for k in range(i):
        matrix[k][0] = k*delete
    for w in range(j):
        matrix[0][w] = w*insert

    for w in range(1,i):
        for x in range(1,j):
            if word1[w] == word2[x]:
                matrix[w][x] = matrix[w-1][x-1]
            else:
                matrix[w][x] = min(matrix[w-1][x] + delete, matrix[w][x-1] + insert, matrix[w-1][x-1] + replace)
    return matrix[i-1][j-1]


for i in range(int(input())):
    word1 = input()
    word2 = input()

    constraint = [int(x) for x in input().split()]
    print(weighted_edit_distance(word1,word2,constraint))

