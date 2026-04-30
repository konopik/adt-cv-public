import numpy as np
import random
import os
class SudokuCreator:
    def __init__(self) -> None:
        self.field = np.zeros([9,9],dtype=int)
    
    def check_sequence(self, sequence: np.ndarray) -> bool:
        seen:set[int] = set()
        without_zeros = sequence[sequence != 0]
        for n in without_zeros:
            seen.add(n)
        return len(seen) == len(without_zeros)


    def check_row(self, row_index: int) -> bool:
        return self.check_sequence(self.field[row_index,:])

    def check_column(self, column_index: int) -> bool:
        return self.check_sequence(self.field[:,column_index])

    def check_block(self, row_index: int, column_index: int) -> bool:
        r_i = (row_index//3)*3
        c_i = (column_index//3)*3
        return self.check_sequence(self.field[r_i:r_i+3,c_i:c_i+3])


    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index) and self.check_column(column_index) and self.check_block(row_index,column_index)
    
    def get_empty(self)->tuple[int,int]|None:
        for i in range(9):
            for j in range(9):
                if self.field[i,j] == 0:
                    return (i,j)
        return None
    
    def create(self)->bool:
            empty = self.get_empty()
            if not empty:
                return True
            row,col = empty
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for n in numbers:
                self.field[row, col] = n
                if self.check_one_cell(row, col):
                    if self.create():
                        return True
            self.field[row, col] = 0
            return False
    
    def puzzle(self,count_of_empty:int):
        count = 0
        while count<count_of_empty:
            i = random.randint(0,8)
            j = random.randint(0,8)
            if self.field[i,j] != 0:
                self.field[i,j] = 0
                count += 1
            
    def csv(self,filepath:str):
        try:
            with open(filepath,'w',encoding='utf8') as f:
                for row in self.field:
                    line = ";".join(map(str, row))
                    f.write(f'{line}\n')
        except FileNotFoundError:
            return

    
    def __str__(self) -> str:
        return str(self.field)

    

path = os.path.join('07-backtracking','sudoku.csv')
        
def main():
    n = int(input('Input count of zeros: '))
    sudokucreator = SudokuCreator()
    if sudokucreator.create():
        sudokucreator.puzzle(n)
        sudokucreator.csv(path)
    print(sudokucreator)

if __name__ == '__main__':
    main()
    



         




