import os
import sys
import timeit
from typing import Callable

def load_customers(shop_path: str) -> list[str]:
    """Načte data z konkrétní cesty a vrací seznam ID zákazníků."""

    customers: list[str] = []

    # Otevření souboru v režimu čtení - "r"
    with open(shop_path, "r", encoding="utf-8") as file:
        try:
            _ = file.readline() # Zbavení se prvního řádku obsahující názvy sloupců v souborech
            lines = file.readlines()
            for line in lines:
                line = line.strip() # Odstranění neviditelných znaků z okrajů řetězce
                splitted = line.split(";") # Rozdělení řádku podle oddělovače -> zde středníku
                time, ckpt, cid, price = splitted
                
                customers.append(cid) # Přidání ID zákazníka do seznamu
        except Exception as e:
            # V případě výskytu chyby v try-bloku, proběhne tento kód
            # Zde konkrétně ošetřuji všechny možné výjimky pomocí obecné Exception
            # Je možné specifikovat pouze na (ValueError, IndexError, ...)
            print(f"Something went wrong: {e}")

    return customers

def check_ckpt_list(customers: list[str]) -> list[str]:
    """Varianta A: vrátí seznam unikátních zákazníků v seznamu."""
    seen: list[str] = []
    
    for customer in customers:
        if customer not in seen:
            seen.append(customer)
    
    return seen


def check_ckpt_set(customers: list[str]) -> set[str]:
    """Varianta B: vrátí množinu unikátních zákazníků v množin."""
    seen: set[str] = set()
    
    for customer in customers:
        seen.add(customer)
    
    return seen


def measure(
    func: Callable[[list[str]], object],
    customers: list[str],
    n_runs: int,
) -> float:
    """Změří čas běhu funkce func(customers) nástrojem timeit."""
    
    return timeit.timeit(lambda: func(customers),number=n_runs)
    


def experiment(data_path: str, city: str, shop: str, day: str = "1-Mon", n_times:int = 50) -> None:
    shop_path = os.path.join(data_path, "output", city, day, f"{shop}.txt")

    print(f"Načítání dat: město={city}, obchod={shop}, den={day}")
    customers = load_customers(shop_path)

    print(f"Počet načtených záznamů: {len(customers)}")

    unique_list = check_ckpt_list(customers)
    unique_set = check_ckpt_set(customers)
    print(f"Počet unikátních zákazníků - list: {len(unique_list)}")
    print(f"Počet unikátních zákazníků - set:  {len(unique_set)}")

    t_list = measure(check_ckpt_list, customers, n_times)
    print(f"Varianta A (list), celkový čas pro {n_times} běhů: {t_list:.4f} s")

    t_set = measure(check_ckpt_set, customers, n_times)
    print(f"Varianta B (set),  celkový čas pro {n_times} běhů: {t_set:.4f} s")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path> [city] [shop] [day]")
        print("Example: python main.py cities Plzeň shop_a 1-Mon")
        sys.exit(1)

    data_path = sys.argv[1]
    # if not os.path.isdir(data_path):
    #     print(f"Error: '{data_path}' is not a directory")
    #     sys.exit(1)

    # Defaultní hodnoty podobně jako v 03-26-market
    city = sys.argv[2] if len(sys.argv) > 2 else "Plzeň"
    shop = sys.argv[3] if len(sys.argv) > 3 else "shop_a"
    day = sys.argv[4] if len(sys.argv) > 4 else "1-Mon"

    experiment(data_path, city, shop, day, n_times=50)


if __name__ == "__main__":
    main()
