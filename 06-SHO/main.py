import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))


def worker_tick(worker: Worker) -> None:
    if worker.timer > 0: # pracovník je zaneprázdněný
        worker.timer -= 1
    elif len(worker.source) > 0: # pokud fronta není prázdná
        person = worker.source.popleft()
        worker.dest.append(person)
        worker.timer = get_delay(period=worker.period, spread_factor=worker.spread_factor)
        print(f"{worker.name} processed a person. Next in {worker.timer} seconds.")


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Current time: {time}")

    for (q_name, q) in queues:
        print(f"{q_name} ({len(q)})")



def main() -> None:
    people_number: int = 1000
    people_in_the_city: deque[list[range]] = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue: deque = deque()    # lide u gate keepera
    vege_queue: deque = deque()    # lide u zeleniny
    cashier_queue: deque = deque() # lide u pokladny
    final_queue: deque = deque()   # lide co odchazeji z obchodu

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [
        ("Street", people_in_the_city),
        ("Gate", gate_queue),
        ("Vege", vege_queue),
        ("Cashier", cashier_queue),
        ("Final", final_queue)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    street_worker = Worker(name="StreetWorker",
                           source=people_in_the_city,
                           dest=gate_queue,
                           period=day_m,
                           spread_factor=0.5)

    gate_worker = Worker(name="GateKeeper",
                         source=gate_queue,
                         dest=vege_queue,
                         period=gate_m,
                         spread_factor=0.1)

    vege_worker = Worker(name="VegeMan",
                         source=vege_queue,
                         dest=cashier_queue,
                         period=vege_m,
                         spread_factor=0.2)

    cashier_worker = Worker(name="Cashier",
                         source=cashier_queue,
                         dest=final_queue,
                         period=final_m,
                         spread_factor=0.5)

    # 3. Hlavní smyčka simulace
    workers = [street_worker, gate_worker, vege_worker, cashier_worker]

    for time in range(2*60*60 + 1): # simulace dvou hodin
        for worker in workers:
            worker_tick(worker=worker)

        if time % 60 == 0: # snapshot každou minutu
            print_snapshot(time=time, queues=queues_to_observe)


if __name__ == "__main__":
    main()
