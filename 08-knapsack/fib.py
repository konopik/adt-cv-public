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

def fib_iter(n: int) -> int | None:
    if n <= 1:
        return n

    # results = [0, 1]
    # for i in range(2, n+1):
    #     new_result = results[i-1] + results[i-2]
    #     results.append(new_result)
    # return results[-1]

    result_curr = 1
    result_last = 0

    for _ in range(2, n+1):
        new = result_curr + result_last
        result_last = result_curr
        result_curr = new
    return result_curr


def main() -> None:
    # lookup: dict[int, int] = {}

    a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    # a = 40 # za jak dlouho se asi dočkáme?

    measure_time(lambda: fib_cache(a), ntimes=100)
    measure_time(lambda: fib_mem(a, lookup={}), ntimes=100)
    # measure_time(lambda: fib(a), ntimes=100)
    measure_time(lambda: fib_iter(a), ntimes=100)



if __name__ == "__main__":
    main()
