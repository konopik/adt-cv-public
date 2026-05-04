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
    if worker.timer>0:
        worker.timer-=1
        return
    if len(worker.source)==0:
        return
    if len(worker.source)>0:
        x=worker.source.popleft()
        worker.dest.append(x)
        worker.timer=get_delay(worker.period,worker.spread_factor)


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"aktualni čas je {time}")
    for que in queues:
        name,q=que
        print(f"{name},{len(q)}")



def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue=deque()
    vege_queue=deque()
    cashier_queue=deque()
    final_queue=deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [
        ("street",people_in_the_city),
        ("gate", gate_queue),
        ("vege",vege_queue),
        ("cashier",cashier_queue),
        ("final",final_queue),
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    street_worker=Worker("streetworker",people_in_the_city,gate_queue,day_m,0.5)
    gate_worker=Worker("gateworker",gate_queue,vege_queue,gate_m,0.5)
    vegeworker=Worker("vegeworkwe",vege_queue,cashier_queue,vege_m,0.5)
    cashworker=Worker("chasworker",cashier_queue,final_queue,final_m,0.5)
    # 3. Hlavní smyčka simulace
    hodiny=int(input())
    for i in range(hodiny*3600+1):
        worker_tick(street_worker)
        worker_tick(gate_worker)
        worker_tick(vegeworker)
        worker_tick(cashworker)
        if i%60==0:
            print_snapshot(i,queues_to_observe)

if __name__ == "__main__":
    main()
