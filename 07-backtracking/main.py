import numpy as np

class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        file_path = file_path.strip()
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                split = line.split(";")
                for y in range(len(split)):
                    split[y] = int(split[y])
                loaded_rows.append(split)

        #print(loaded_rows)
        # convert nested list to numpy array
        self.field = np.array(loaded_rows)

    def check_sequence(self, sequence: np.ndarray) -> bool:
        sequence_non_zero = sequence[sequence != 0]
        return len(sequence_non_zero) == len(set(sequence_non_zero))

    def check_row(self, row_index: int) -> bool:
        return self.check_sequence(self.field[row_index,:])

    def check_column(self, column_index: int) -> bool:
        return self.check_sequence(self.field[:,column_index])

    def check_block(self, row_index: int, column_index: int) -> bool:
        row_index = (row_index//3) * 3
        column_index = (column_index//3) * 3
        block = self.field[row_index:row_index+3,column_index:column_index+3].reshape(-1)
        return self.check_sequence(block)

    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index) and self.check_column(column_index) and self.check_block(row_index,column_index)

    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        for col in range(self.field.shape[0]):
            for row in range(self.field.shape[1]):
                if self.field[row,col] == 0:
                    return row,col
        return None

    def solve(self) -> bool:
        """ Recursively solves the sudoku. """

        empty_cell = self.get_empty_cell()

        if not empty_cell:
            return True
        row,col = empty_cell
        for val in range(9):
            self.field[row, col] = val+1
            if self.check_one_cell(row,col) and self.solve():
                return True

        #Important line
        self.field[row,col] = 0
        return False

def test_sudoku(file: str) -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load(file)
    print(f"Before: \n{sudoku_solver.field}")
    print(" ")
    if sudoku_solver.solve():
        print(f"After: \n{sudoku_solver.field}")
    else:
        print("Cooked!")

def main() -> None:
    test_sudoku("07-backtracking/sudoku.csv")
    print(" ")
    test_sudoku("07-backtracking/sudoku_null.csv")


if __name__ == "__main__":
    print(" ")
    main()
    print(" ")
