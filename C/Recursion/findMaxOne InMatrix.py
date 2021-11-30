
def count(mat, i, j, mask):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
        return 0
    if mat[i][j] == 0 or mask[i][j] == True:
        return 0
    mask[i][j] = True
    return 1 + count(mat, i - 1, j, mask) + count(mat, i, j-1, mask) + count(mat, i + 1, j, mask) + count(mat, i, j+1, mask) + count(mat, i-1, j-1, mask) + count(mat, i+1, j+1, mask) + count(mat, i-1, j+1, mask) + count(mat, i+1, j-1, mask)

def findMax(mat=[]):
    global res
    mask = [ [False for i in range(len(mat[0]))] for i in range(len(mat)) ]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] is 1 and not mask[i][j]:    
                c = count(mat, i, j, mask)
                print(i, j, c)
                if c > res:
                    res = c






mat = [
    [1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
res = 0

findMax(mat)
print(res)