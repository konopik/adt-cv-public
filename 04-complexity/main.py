import os
import sys
import timeit
from typing import Iterable, Callable

N_RUNS = 5


def iter_checkpoints(shop_path: str) -> list[str]:
    """Načte data z konkrétní cesty a vrací páry (ckpt, id_zákazníka).

    Poznámka: Pokud bychom vraceli pouze ckpt (názvy checkpointů),
    bylo by jich jen ~20 unikátních, což je příliš málo na viditelný rozdíl.
    """
    customers:list[str] = []
    try:
        with open(shop_path,'r',encoding='utf8') as f:
            next(f)
            for line in f:
                line.strip()
                splitted = line.split(';')
                time, ckpt, cid, price = splitted
                customers.append(cid)
    except Exception as e:
        print(f'Something wrong {e}')

    return customers


def check_ckpt_list(shop_path: str) -> list[str]:
    """Varianta A: vrátí seznam unikátních párů (checkpoint, zákazník) pomocí listu."""
    seen: list[str] = []
    return seen


def check_ckpt_set(shop_path: str) -> set[tuple[str, str]]:
    """Varianta B: vrátí množinu unikátních párů (checkpoint, zákazník) pomocí setu."""
    seen: set[tuple[str, str]] = set()
    return seen


def measure(func: Callable, shop_path: str, n_runs: int = N_RUNS) -> float:
    """Změří čas běhu funkce func(shop_path) pomocí timeit."""
    return -1.0


def experiment(data_path: str, city: str, shop: str, day: str = "1-Mon") -> None:
    shop_path = os.path.join(data_path, city, day, f"{shop}.txt")

    print(f"Načítání dat: město={city}, obchod={shop}, den={day}")
    unique_list = check_ckpt_list(shop_path)
    unique_set = check_ckpt_set(shop_path)
    print(f"Počet unikátních párů (checkpoint, zákazník) - list: {len(unique_list)}")
    print(f"Počet unikátních párů (checkpoint, zákazník) - set:  {len(unique_set)}")

    t_list = measure(check_ckpt_list, shop_path)
    print(f"Varianta A (list), celkový čas pro {N_RUNS} běhů: {t_list:.4f} s")

    t_set = measure(check_ckpt_set, shop_path)
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
