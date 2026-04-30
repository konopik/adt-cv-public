from collections import defaultdict

# Testovací data: Jméno čtenáře, ID čtenáře, ISBN, Pobočka
# Takto mohou vypadat záznamy načtené z CSV nebo databáze.
raw_data: list[tuple[str, str, str, str]] = [
    ("Anna Malá", "R-0001", "9788027100001", "Centrum"),
    ("Bohuslav Hruška", "R-0002", "9788027100002", "Centrum"),
    ("Anna Malá", "R-0001", "9788027100003", "Sever"),
    ("Cyril Veselý", "R-0003", "9788027100004", "Jih"),
    ("Dana Krátká", "R-0004", "9788027100005", "Sever"),
    ("Hana Blažková", "R-0009", "9788027100010", "Západ"),
    ("Ivan Král", "R-0010", "9788027100011", "Západ"),
    ("Anna Malá", "R-0001", "9788027100012", "Centrum"),
    ("Dana Krátká", "R-0004", "9788027100013", "Sever"),
    ("Jitka Jelínková", "R-0011", "9788027100014", "Východ"),
]


def group_rentals_by_branch(data: list[tuple[str, str, str, str]]) -> dict[str, list[str]]:
    """Vrátí tabulku, kde klíčem je pobočka a hodnotou seznam ISBN knih,
    které byly na pobočce vypůjčeny.
    """
    tab=defaultdict()
    for person in data:
        name,ID,ISBN,where=person
        if where in tab:
            tab[where].append(ISBN)
        else:
            tab[where]=[ISBN]

    return tab

def main():
    print("--- Vypůjčky dle poboček ---")
    rentals_by_branch = group_rentals_by_branch(raw_data)
    for branch, isbns in rentals_by_branch.items():
        print(f"{branch}: {len(isbns)} vypůjček")
        print(f"  {isbns}") 




if __name__ == "__main__":
    main()
