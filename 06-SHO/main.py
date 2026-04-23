
import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float 
    timer: int = 0
    current_cust:int|None = None


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))



def worker_tick(worker: Worker) -> None:
    if worker.timer > 0:
        worker.timer -= 1
        if worker.timer == 0 and worker.current_cust is not None:
            worker.dest.append(worker.current_cust)
            worker.current_cust = None
        return
    
    if worker.source:
        worker.current_cust = worker.source.popleft()
        delay = get_delay(worker.period, worker.spread_factor)
        worker.timer = max(1,delay)


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(time,end='')
    for name,q in queues:
        print(f',{name}({len(q)})',end='')
    print()


def main() -> None:
    people_number = 100
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue = deque()
    vege_queue = deque()
    final_queue = deque()
    finished_people = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [("Město", people_in_the_city),
        ("Vstup", gate_queue),
        ("Zelenina", vege_queue),
        ("Pokladna", final_queue),
        ("Domů", finished_people)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 5  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2*60  # Pokladna zabere 2 minuty
    sf = 0.25

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    workers = [
        Worker("Ulice", people_in_the_city, gate_queue, day_m,sf),
        Worker("Vrátný", gate_queue, vege_queue, gate_m,sf),
        Worker("Zelinář", vege_queue, final_queue, vege_m,sf),
        Worker("Pokladní", final_queue, finished_people, final_m,sf)
    ]

    time = 0
    # 3. Hlavní smyčka simulace
    time = 3600*2
    for t in range(time+1):
        if t%(60*2) == 0:
            print_snapshot(t,queues_to_observe)
        for w in workers:
            worker_tick(w)
        

        if time % 60 == 0:
            print_snapshot(time, queues_to_observe)

    print(vege_queue)
    
if __name__ == "__main__":
    main()
