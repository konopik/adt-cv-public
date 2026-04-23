import functools

from utils import measure_time


def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

@functools.cache
def fib_cache(n: int) -> int:
    # TODO implementujte s functools.cache.
    return 0

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    # TODO implementujte s explicitní pamětí.
    return 0

  

def fib_iter2(n: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b

def main() -> None:
    lookup: dict[int, int] = {}

    # a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    a = 90 # za jak dlouho se asi dočkáme? Nikdy

    measure_time(lambda: fib_cache(a), 100)
    measure_time(lambda: fib_mem(a, {}), 100)
    measure_time(lambda: fib_iter2(a), 100)
    #measure_time(lambda: fib(a))
    
    print(fib_cache(a))


if __name__ == "__main__":
    main()
