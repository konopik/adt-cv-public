import numpy as np

class SudokuSolverX:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, filename: str):
        with open(filename, "r", encoding="UTF-8") as file:
            loaded_rows: list [list[int]] = []
            lines = file.readlines()
            for line in lines:
                cisla = line.strip().split(";")
                numbers:list[int] = []
                for num in cisla:
                    int_num = int(num)
                    numbers.append(int_num)
                loaded_rows.append(numbers)
        self.field = np.array(loaded_rows)

    def check_sequence(self, sequence: np.ndarray) -> bool:
        mnozina: set[int] = set()
        for i in sequence:
            if i == 0:
                continue
            if i not in mnozina:
                mnozina.add(i)
                continue
            return False
        return True

    # check_row, check_column a check_block zůstávají stejné...
    def check_row(self, row_index: int) -> bool:
        row_data = self.field[row_index, :]
        return self.check_sequence(row_data)

    def check_column(self, col_index: int) -> bool:
        col_data = self.field[:, col_index]
        return self.check_sequence(col_data)

    def check_block(self, row_index: int, col_index: int) -> bool:
        # ÚKOL: Upravte výpočet počátku bloku a řez pro 2x2 bloky
        row_start = (row_index // 3) * 3
        col_start = (col_index // 3) * 3

        podmatice = self.field[row_start: row_start + 3, col_start : col_start + 3]
        zplostela_podm = podmatice.reshape(-1)
        return self.check_sequence(zplostela_podm)

    def check_diagonals(self, row_index: int, col_index: int) -> bool:
        """
        ÚKOL:
        1. Zjistěte, zda buňka [row_index, col_index] leží na hlavní diagonále (shora dolů). 
           Pokud ano, zkontrolujte ji pomocí check_sequence.
        2. Zjistěte, zda leží na vedlejší diagonále (zdola nahoru).
           Pokud ano, zkontrolujte ji.
        Nápověda: np.diag() nebo prostý cyklus / indexování.
        """
        
        # Hlavní diagonála ( \ )
        if row_index == col_index:
            # Jak získám celou hlavní diagonálu z self.field?
            main_diag = np.diag(self.field)
            if not self.check_sequence(main_diag):
                return False

        # Vedlejší diagonála ( / )
        if row_index + col_index == 8:
            # Jak získám vedlejší diagonálu? (např. pomocí překlopení matice nebo ručně)
            # fliplr převrátí matici zrcadlově, takže z / udělá \
            side_diag = np.diag(np.fliplr(self.field))
            if not self.check_sequence(side_diag):
                return False
        
        return True

    def check_one_cell(self, row_index: int, col_index: int) -> bool:
        # ÚKOL: Musíte integrovat novou kontrolu diagonál
        row_ok = self.check_row(row_index)
        col_ok = self.check_column(col_index)
        block_ok = self.check_block(row_index, col_index)
        diag_ok = self.check_diagonals(row_index, col_index)
        
        return row_ok and col_ok and block_ok and diag_ok

    # solve a get_empty_cell zůstávají stejné...

    def get_empty_cell(self) -> tuple[int, int] | None:
        for r in range(self.field.shape[0]):
            for c in range(self.field.shape[1]):
                if self.field[r, c] == 0:
                    return r, c
        return None
    
    def solve(self) -> bool:
        next_cell = self.get_empty_cell()
        if next_cell == None:
            return True
        
        row, col = next_cell
        
        # ÚKOL: Upravte rozsah zkoušených čísel pro 4x4
        for num in range(1, 10):
            self.field[row, col] = num
            if self.check_one_cell(row, col):
                if self.solve():
                    return True
            
        self.field[row, col] = 0
        return False

def main() -> None:
    sudoku_solver = SudokuSolverX()
    sudoku_solver.load("sudoku_3.csv")
    sudoku_solver.solve()
    print(sudoku_solver.field)
    
if __name__ == "__main__":
    main()