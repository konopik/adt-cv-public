import functools

from utils import measure_time


def fib(n: int) -> int:
    # TODO implementujte.
    return 0

@functools.cache
def fib_cache(n: int) -> int:
    # TODO implementujte s functools.cache.
    return 0

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    # TODO implementujte s explicitní pamětí.
    return 0

def fib_pre(n: int) -> int:
    if n <= 1:
        return n
    lookup: list[int] = [0]*(n+1)
    lookup[0] = 0
    lookup[1] = 1
    for i in range(2,n+1):
        lookup[i] = lookup[i-1] + lookup[i-2]

    return lookup[n]

def main() -> None:
    #lookup: dict[int, int] = {}

    a = 500

    measure_time(lambda: fib_cache(a), 1)
    measure_time(lambda: fib_mem(a, lookup = {}), 1)
    measure_time(lambda: fib_pre(a), 1)
    # measure_time(lambda: fib(a))



    # print(fib_pre(a))
    # print(fib_mem(a, lookup))


if __name__ == "__main__":
    main()
