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

def fib_iter(n: int) -> int:
    # TODO implementujte výpočtem zdola nahoru.    
    return 0

def main() -> None:
    lookup: dict[int, int] = {}

    # a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    a = 90 # za jak dlouho se asi dočkáme? Nikdy

    measure_time(lambda: fib_cache(a), 100) # zkreslené, nemažeme cache
    measure_time(lambda: fib_mem(a, {}), 100)
    measure_time(lambda: fib_iter(a), 100)
    measure_time(lambda: fib(a))


if __name__ == "__main__":
    main()
