import functools

from utils import measure_time


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@functools.cache
def fib_cache(n: int) -> int:
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    if n <= 1:
        return n

    if n not in lookup:
        lookup[n] = fib_mem(n - 1,lookup) + fib_mem(n - 2,lookup)

    return lookup[n]

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
