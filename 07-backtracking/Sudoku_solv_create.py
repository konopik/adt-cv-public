import numpy as np
import random
import timeit
class Sudoku:
    def __init__(self) -> None:
        self.field = np.zeros([9,9],dtype=int)
        return
    def get_empty(self)->tuple[int,int]|None:
        for i in range(9):
            for j in range(9):
                if self.field[i,j] == 0:
                    return (i,j)
        return
    
    def check_sequence(self,sequence:np.ndarray)->bool:
        seen:set[int] = set()
        without_zeros = sequence[sequence!=0]
        for number in without_zeros:
            seen.add(number)
        return len(without_zeros) == len(seen)
    
    def check_row(self,n:int)->bool:
        return self.check_sequence(self.field[n,:])
    
    def check_column(self,n:int)->bool:
        return self.check_sequence(self.field[:,n])
    
    def check_block(self,row:int,col:int)->bool:
        row_index = (row//3)*3
        col_index = (col//3)*3
        return self.check_sequence(self.field[row_index:row_index+3,col_index:col_index+3])
    
    def check_one_cell(self,row:int,col:int)->bool:
        return self.check_row(row) and self.check_column(col) and self.check_block(row,col)
    
    def generate_canvas(self)->bool:
        empty_cell = self.get_empty()
        if not empty_cell:
            return True
        row,col = empty_cell
        numbers = [n for n in range(1,10)]
        random.shuffle(numbers)
        for n in numbers:
            self.field[row,col] = n
            if self.check_one_cell(row,col):
                if self.generate_canvas():
                    return True
        self.field[row,col] = 0
        return False
    
    def generate_puzzle(self,n:int)->bool:
        if n<0 or n>81:
            return False
        sum_of_zeros = 0
        if self.generate_canvas():
            while sum_of_zeros < n:
                row = random.randint(0,8)
                col = random.randint(0,8)
                if self.field[row,col] != 0:
                    self.field[row,col] = 0
                    sum_of_zeros += 1
            return True
        return False
    
    def solve_puzzle(self)->bool:
        empty_cell = self.get_empty()
        if not empty_cell:
            return True
        row,col = empty_cell
        numbers = [n for n in range(1,10)]
        for n in numbers:
            self.field[row,col] = n
            if self.check_one_cell(row,col):
                if self.solve_puzzle():
                    return True
        self.field[row,col] = 0
        return False
    
    def __str__(self) -> str:
        return str(self.field)
    

def main():
    sudoku_objeckt = Sudoku()
    numbers = [n for n in range(1,90,20)]
    round = 1
    longest_dur = 0
    longest_round = 0
    longest_n = 0
    for n in numbers:
        if sudoku_objeckt.generate_puzzle(n) and sudoku_objeckt.solve_puzzle():
            duration = timeit.timeit(sudoku_objeckt.solve_puzzle)
            if duration > longest_dur:
                longest_dur = duration
                longest_round = round
                longest_n = n
            print(f'Round:{round} for n={n}')
            print(sudoku_objeckt.field)
            print(f'Duration: {duration}')
            round += 1
    print(f'Longest duration: {longest_dur} in round: {longest_round} for n: {longest_n}')

if __name__=='__main__':
    main()