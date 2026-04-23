import os
import sys
import timeit
from typing import Callable

N_RUNS = 5

def load_customers(shop_path: str) -> list[str]:
    """Načte data z konkrétní cesty a vrací seznam ID zákazníků."""
    list_customers = []
    with open(shop_path, "r" , encoding="utf-8") as f:
        _ = f.readline()
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            split_line = line.split(";")
            time, ckpt, cid, money = split_line
            list_customers.append(cid)
    return list_customers


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
    n_runs: int = N_RUNS,
) -> float:
    """Změří čas běhu funkce func(customers) nástrojem timeit."""
    """
    def func_wrapper() -> None:
        func(customers)
    return timeit.timeit(stmt=func_wrapper, number=n_runs)
    """
    return timeit.timeit(stmt=lambda: func(customers), number=n_runs)


def experiment(data_path: str, city: str, shop: str, day: str = "1-Mon") -> None:
    shop_path = os.path.join(data_path, "output", city, day, f"{shop}.txt")

    print(f"Načítání dat: město={city}, obchod={shop}, den={day}")
    customers = load_customers(shop_path)

    print(f"Počet načtených záznamů: {len(customers)}")

    unique_list = check_ckpt_list(customers)
    unique_set = check_ckpt_set(customers)
    print(f"Počet unikátních zákazníků - list: {len(unique_list)}")
    print(f"Počet unikátních zákazníků - set:  {len(unique_set)}")

    t_list = measure(check_ckpt_list, customers)
    print(f"Varianta A (list), celkový čas pro {N_RUNS} běhů: {t_list:.4f} s")

    t_set = measure(check_ckpt_set, customers)
    print(f"Varianta B (set),  celkový čas pro {N_RUNS} běhů: {t_set:.4f} s")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path> [city] [shop] [day]")
        print("Example: python main.py cities Plzeň shop_a 1-Mon")
        sys.exit(1)

    data_path = sys.argv[1]
    if not os.path.isdir(data_path):
        print(f"Error: '{data_path}' is not a directory")
        sys.exit(1)

    # Defaultní hodnoty podobně jako v 03-26-market
    city = sys.argv[2] if len(sys.argv) > 2 else "Plzeň"
    shop = sys.argv[3] if len(sys.argv) > 3 else "shop_a"
    day = sys.argv[4] if len(sys.argv) > 4 else "1-Mon"

    experiment(data_path, city, shop, day)


if __name__ == "__main__":
    main()
