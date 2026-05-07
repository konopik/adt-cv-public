import os

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        #  implement loading of the file

        # convert nested list to numpy array
        try:
            with open(file_path,'r',encoding='utf8') as f:

                for line in f:
                    linenum:list[int] = []
                    numbers = line.split(';')
                    try:
                        for n in numbers:
                            linenum.append(int(n))
                    except ValueError:
                        continue
                    
                    loaded_rows.append(linenum)
        except FileNotFoundError:
            pass


        self.field = np.array(loaded_rows)



    def check_sequence(self, sequence: np.ndarray) -> bool:
        seen:set[int] = set()
        without_zeros = sequence[sequence != 0]
        for n in without_zeros:
            seen.add(n)
        return len(seen) == len(without_zeros)

    def check_row(self, row_index: int) -> bool:
        return self.check_sequence(sequence=self.field[row_index,:])

    def check_column(self, column_index: int) -> bool:
        return self.check_sequence(sequence=self.field[:,column_index])

    def check_block(self, row_index: int, column_index: int) -> bool:
        row_s_i = (row_index//3) *3
        collumn_s_i = (column_index//3) *3
        return self.check_sequence(sequence=self.field[row_s_i:row_s_i+3,collumn_s_i:collumn_s_i+3])

    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index=row_index) and self.check_column(column_index=column_index) and self.check_block(row_index=row_index,column_index=column_index)

    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        for row in range(9):
            for col in range(9):
                if self.field[row,col] == 0:
                    return (row,col)
        return None

    def solve(self) -> bool:
        """ Recursively solves the sudoku. """
        empty_cell = self.get_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell

        for v in range(1,10):
            self.field[row,col] = v
            if self.check_one_cell(row_index=row,column_index=col):
                if self.solve():
                    return True
        self.field[row,col] = 0

        return False
    
    def __str__(self)->str:
        return(str(self.field))






def main() -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load(file_path=os.path.join('07-backtracking','sudoku.csv'))
    print(sudoku_solver)
    if sudoku_solver.solve():
        print(sudoku_solver)
    else:
        print('Chyba')

if __name__ == "__main__":
    main()
