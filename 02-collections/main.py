from dataclasses import dataclass

# Testovací data: Jméno, Osobní číslo, Předmět
# Takto vypadají data načtená například z CSV souboru nebo databáze.
raw_data = [
    ("Jan Novák", "A01N001", "Matematika"),
    ("Petr Svoboda", "A01N002", "Fyzika"),
    ("Jan Novák", "A01N001", "Fyzika"),
    ("Marie Dvořáková", "A01N003", "Informatika"),
    ("Petr Svoboda", "A01N002", "Matematika"),
    ("Jana Černá", "A01N004", "Matematika"),
    ("Karel Nový", "A01N005", "Angličtina"),
    ("Marie Dvořáková", "A01N003", "Angličtina"),
]


class Student:
    name: str
    os_cislo: str

    def __init__(self, name: str, os_cislo: str):
        self.name = name
        self.os_cislo = os_cislo
        
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.os_cislo == other.os_cislo and self.name == other.name
    
    def __hash__(self):
        return hash((self.os_cislo, self.name))
    
    def __repr__(self) -> str:
        return f"Student(name='{self.name}', os_cislo='{self.os_cislo}')"

def get_unique_subjects(data: list[tuple[str, str, str]]) -> set[str]:
    """
    Vrátí množinu unikátních předmětů.
    """
    unique_subjects = set()

    for data_line in data:
        unique_subjects.add(data_line[2])

    return unique_subjects # PLACEHOLDER

def group_students_by_subject(data: list[tuple[str, str, str]]) -> dict[str, list[Student]]:
    """
    Vrátí slovník, kde klíčem je předmět a hodnotou seznam studentů (instancí třídy Student),
    kteří jsou na předmět zapsáni.
    """
    subject_students : dict[str, list[Student]] = {}
    for data_line in data:
        student = Student(data_line[0], data_line[1])

        if data_line[2] in subject_students:
            subject_students[data_line[2]].append(student)
        else:
            subject_students[data_line[2]] = [student]

    return subject_students 

def get_unique_students(data: list[tuple[str, str, str]]) -> set[Student]:
    """
    Vrátí množinu unikátních studentů.
    Pozor: Data obsahují duplicity (jeden student může mít více předmětů).
    Cílem je získat množinu fyzických osob.
    """
    unique_students = set()

    for data_line in data:
        student = Student(data_line[0], data_line[1])
        unique_students.add(student)
    
    return unique_students # PLACEHOLDER

def main() -> None:
    print("--- ÚKOL 1: Unikátní předměty ---")
    subjects = get_unique_subjects(raw_data)
    print(f"Nalezené předměty: {subjects}")

    print("\n--- ÚKOL 2: Studenti dle předmětů ---")
    by_subject = group_students_by_subject(raw_data)
    for subject, students in by_subject.items():
        print(f"{subject}: {len(students)} studentů")
        # print(f"  {students}") # Pro detailní výpis

    print("\n--- ÚKOL 3: Unikátní studenti (Množina) ---")
    unique_students = get_unique_students(raw_data)
    print(f"Počet unikátních studentů: {len(unique_students)}")
    print(unique_students)

    # Kontrola správnosti implementace __eq__ a __hash__
    # V raw_data je 8 záznamů, ale jen 5 unikátních studentů (A101, A102, A103, A104, A105)
    expected_count = 5
    if len(unique_students) == expected_count:
        print(f"\n[OK] Počet studentů odpovídá očekávání ({expected_count}).")
    else:
        print(f"\n[CHYBA] Očekáváno {expected_count} studentů, nalezeno {len(unique_students)}.")
        print("Tip: Funguje správně porovnávání instancí třídy Student v množině?")

if __name__ == "__main__":
    main()
