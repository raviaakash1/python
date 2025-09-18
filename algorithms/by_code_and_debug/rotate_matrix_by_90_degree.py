from typing import List

def transponse(matrix: List[List[int]]) -> List[List[int]]:
    # transpose the matrix
    row: int = len(matrix)
    col: int = len(matrix[0])
    new_matrix: List[List[int]] = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def rotate_array(matrix: List[List[int]]) -> List[List[int]]:
    new_matrix: List[List[int]] = transponse(matrix)
    print_matrix(new_matrix)
    new_m: List[List[int]] = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    row = len(new_matrix)
    col = len(new_matrix[0])
    for i in range(row):
        for j in range(col-1,-1, -1):
            new_m[j][i] = new_matrix[i][j]
            
def print_matrix(matrix):
    row: int = len(matrix)
    col: int = len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = " ")
        print()

if __name__ == "__main__":
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    result: List[List[int]] = rotate_array(matrix)