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
    if worker.timer > 0:
        worker.timer -= 1
    elif len(worker.source) > 0:
            person = worker.source.popleft()
            worker.dest.append(person)
            worker.timer = get_delay(worker.period, worker.spread_factor)



def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Actual time: {time} seconds")
    
    for name, queue in queues:
        print(f"\t{name}: {len(queue)} people")


def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue : deque  = deque()  # Lidé čekající u gate keepera
    vege_queue : deque  = deque()  # Lidé čekající na vážení zeleniny
    cashier_queue : deque  = deque()  # Lidé čekající na pokladnu
    final_queue : deque  = deque()  # Lidé odcházející z obchodu
    


    # Seznam pro výpis (jméno, fronta)
    queues_to_observe : list[tuple[str, deque]] = [
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
    street_worker = Worker("Street", people_in_the_city, gate_queue, day_m, 0.5)
    gate_worker = Worker("Gate", gate_queue, vege_queue, gate_m, 0.1)
    vege_worker = Worker("Vege", vege_queue, cashier_queue, vege_m, 0.2)
    cashier_worker = Worker("Cashier", cashier_queue, final_queue, final_m, 0.3)    

    time = 0
    # 3. Hlavní smyčka simulace
    for time in range(2 * 60 * 60+1):  # Simulace 2 hodin 
        for worker in [street_worker, gate_worker, vege_worker, cashier_worker]:
            worker_tick(worker)

        if time % 60 == 0:
            print_snapshot(time, queues_to_observe)

    print(vege_queue)
    
if __name__ == "__main__":
    main()
