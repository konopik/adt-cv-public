from utils import measure_time
import os


# load data 2.616 1:32   ->  score is value, time is weight
def load_data(path: str) -> tuple[list[float], list[int]]:
    values: list[float] = [] # rating
    weights: list[int] = [] # délky v sekundách

    with open(path, encoding="utf-8") as f:
        for line in f:
            score, time = line.split(" ")
            values.append(float(score))

            mins, sec = time.split(":")
            weights.append(int(mins) * 60 + int(sec))

    return values, weights


def knapsack_backtrack(capacity: int, weights: list[int], values: list[float],
                       n: int) -> float:
    # jsem na dně   or   nezbývá místo
    if n == len(weights) or capacity == 0:
        return 0.0

    # vejde se tam to, co tam chci dát?
    if weights[n] > capacity:
        # nevejde -> tak to tam prostě nedáme -- nemáme na výběr
        return knapsack_backtrack(capacity, weights, values, n + 1)

    # vejde -> rozhoduji se [dáme/nedáme]. Součástí řešení je to, co se nám víc vyplatí
    next_capacity = capacity - weights[n]

    with_item = values[n] + knapsack_backtrack(next_capacity, weights, values, n + 1)
    without_item = knapsack_backtrack(capacity, weights, values, n + 1)

    return max(with_item, without_item)


def knapsack_mem(capacity: int, weights: list[int], values: list[float], n: int,
                 mem: dict[tuple[int, int], float]) -> float:
    # jsem na dně   or   nezbývá místo
    if n == len(weights) or capacity == 0:
        return 0

    ## pokud to mám v paměti tak to jen vrátím
    ## DP CODE
    if (n, capacity) in mem:
        return mem[(n, capacity)]

    # vejde se tam to, co tam chci dát?
    if weights[n] > capacity:
        # nevejde -> tak to tam prostě nedáme -- nemáme na výběr
        solution = knapsack_mem(capacity, weights, values, n + 1, mem)
        mem[(n, capacity)] = solution  ## DP CODE
        return solution

    # vejde -> rozhoduji se [dáme/nedáme]. Součástí řešení je to, co se nám víc vyplatí
    next_capacity = capacity - weights[n]

    with_item = values[n] + knapsack_mem(next_capacity, weights, values, n + 1, mem)
    without_item = knapsack_mem(capacity, weights, values, n + 1, mem)

    solution = max(with_item, without_item)

    mem[(n, capacity)] = solution  ## DP CODE
    return solution


def main() -> None:
    directory = '08-knapsack'
    data = 'data'
    file = 'songs copy.txt'
    path = os.path.join(directory,data,file)
    values, weights = load_data(path=path)
    capacity = 4 * 60 # čtyři minuty

    mem: dict[tuple[int, int], float] = {}

    print(measure_time(lambda: knapsack_mem(capacity, weights, values, 0, mem)))
    print(measure_time(lambda: knapsack_backtrack(capacity, weights, values, 0)))

if __name__ == "__main__":
    main()
