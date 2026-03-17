from dataclasses import dataclass
from collections import defaultdict
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

@dataclass(frozen=True)
class Student:
    name: str
    os_cislo: str

def get_unique_subjects(data: list[tuple[str, str, str]]) -> set[str]:
    """
    Vrátí množinu unikátních předmětů.
    """
    subject_set:set[str] = set()
    for T in data:
        subject = T[2]
        subject_set.add(subject)
    return subject_set # PLACEHOLDER

def group_students_by_subject(data: list[tuple[str, str, str]]) -> dict[str, list[Student]]:
    """
    Vrátí slovník, kde klíčem je předmět a hodnotou seznam studentů (instancí třídy Student),
    kteří jsou na předmět zapsáni.
    """
    students:dict[str,list[Student]] = dict()
    for T in data:
        name,number,subject = T[0],T[1],T[2]
        if subject not in students.keys():
            students[subject] = []
        students[subject].append(Student(name,number))
    return students
        
        
        
    return {} # PLACEHOLDER

def get_unique_students(data: list[tuple[str, str, str]]) -> set[Student]:
    """
    Vrátí množinu unikátních studentů.
    Pozor: Data obsahují duplicity (jeden student může mít více předmětů).
    Cílem je získat množinu fyzických osob.
    """
    studentset:set[Student] = set()
    for T in data:
        name,number = T[0],T[1]
        studentset.add(Student(name,number))
    return studentset # PLACEHOLDER

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
