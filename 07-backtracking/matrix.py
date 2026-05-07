import numpy as np
import timeit
def convert(mat:list[list[int]])->np.ndarray:
    return np.array(mat)

def det(matrix:np.ndarray)->int:
    ob_shape = matrix.shape
    row,col = ob_shape
    if row == 1:
        return matrix[0,0]
    if row == 2:
        d = (matrix[0,0]*matrix[1,1])-(matrix[1,0]*matrix[0,1])
        return d
    d = 0
    for i in range(row):
        element = matrix[i,0]
        if element == 0:
            continue
        symbol = (-1)**i
        submatrix = np.delete(matrix,i,axis=0)
        submatrix = np.delete(submatrix,0,axis=1)
        d += element*symbol*(det(submatrix))
    return d


def det_faster(matrix:np.ndarray)->float:
    matrix = matrix.astype(float).copy()
    ob_shape = matrix.shape
    row,col = ob_shape
    
    if row == 1:
        return matrix[0,0]
    if row == 2:
        return (matrix[0,0]*matrix[1,1])-(matrix[1,0]*matrix[0,1])
    
    if matrix[0,0] == 0:
        for i in range(1,row):
            if matrix[i,0] != 0:
                matrix[0,:],matrix[i,:] = matrix[i,:],matrix[0,:]
                return -det_faster(matrix)
        return 0.0
    element = matrix[0,0]       
    for i in range(1,row):
        multiplicatior = -(matrix[i,0])/element
        matrix[i,:] += multiplicatior*matrix[0,:]
    submatrix = np.delete(matrix,0,axis=0)
    submatrix = np.delete(submatrix,0,axis=1)
    return element*det_faster(submatrix)

    
def gcd(a:int,b:int)->int:
    if a == 0 or b == 0:
        return 0
    a_set:set[int] = set()
    b_set:set[int] = set()
    for i in range(1,abs(a)+1):
        if a%i == 0:
            a_set.add(i)
    for j in range(1,abs(b)+1):
        if b%j == 0:
            b_set.add(j)
    together:set[int] = a_set.intersection(b_set)
    max_v = max(together)
    return max_v

def primary(a:int)->bool:
    a_set:set[int] = set()
    for i in range(1,a+1):
        if a%i == 0:
            a_set.add(i)
    if len(a_set) == 2:
        return True
    return False


def main():
    A = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = convert(A)
    d = det(matrix)
    d_fast = det_faster(matrix)
    print(f'Klasicky zpusob - vysledek={d}\nrychlejsi zpusob - vysledek={d_fast}')

    
    n = gcd(107,52)
    print(f'gdc = {n}')

    q = 13
    if primary(q):
        print(f'{q} is primary')
    else:
        print(f'{q} is not primary')


if __name__=='__main__':
    main()

    

            
