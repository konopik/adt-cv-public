import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.5
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    time = int(random.gauss(period, period * spread_factor))
    if time < 1:
        return 1
    return time


def worker_tick(worker: Worker) -> None:
    if worker.timer > 0:
        worker.timer -= 1
    elif len(worker.source) > 0:
        customer = worker.source.popleft()
        worker.dest.append(customer)
        worker.timer = get_delay(worker.period, worker.spread_factor)
        # print(f"{worker.name} processed a person. Next in {worker.timer} seconds.")


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Actual time: {time//60} minutes")
    for name, queue in queues:
        print(f"{name}:{len(queue)} people")
    # \t

def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue: deque = deque()
    vegetable_queue: deque = deque()
    cashier_queue: deque = deque()
    final_queue: deque = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [("Street", people_in_the_city),
                         ("Gate",gate_queue),
                         ("Vegetable",vegetable_queue),
                         ("Cashier",cashier_queue),
                         ("Final",final_queue)]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 5s
    vegetable_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    street_worker = Worker("Street_worker", people_in_the_city, gate_queue, day_m)
    gate_worker = Worker("Gate_worker", gate_queue, vegetable_queue, gate_m)
    vegetable_worker = Worker("Vegetable_worker", vegetable_queue, cashier_queue, vegetable_m)
    cashier_worker = Worker("Cashier_worker", cashier_queue, final_queue, final_m)

    time = 0
    # 3. Hlavní smyčka simulace
    for i in range(2*3600 + 0*60 + 0):
        for worker in [street_worker, gate_worker, vegetable_worker, cashier_worker]:
            worker_tick(worker)

        if i%120 == 0:
            print_snapshot(i, queues_to_observe)
            print(" ")

    print_snapshot(7200, queues_to_observe)
    # print(f"People in vegetable queue: {len(vegetable_queue)}")

    print(vege_queue)
    
if __name__ == "__main__":
    main()
    print(" ")
    print("DONE")
