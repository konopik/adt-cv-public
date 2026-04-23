import functools

from utils import measure_time


def fib(n: int) -> int:
    # TODO implementujte.
    return 0

@functools.cache
def fib_cache(n: int) -> int:
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)
#b
def fib_mem(n: int, lookup: dict[int, int]) -> int:
    # TODO implementujte s explicitní pamětí.
    return 0

def fib_iter(n: int) -> int:
    # TODO implementujte výpočtem zdola nahoru.    
    return 0

def fib_fast(n:int)->int | None:
    if n<=1:
        return n
    fib_list=[0]*(n+1)
    fib_list[0]=0
    fib_list[1]=1
    for i in range(2,n+1):
        fib_list[i]=(fib_list[i-1]+fib_list[i-2])
    return fib_list[n]

def main() -> None:
    a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    # a = 40 # za jak dlouho se asi dočkáme?

    measure_time(lambda: fib_cache(a), 100) # zkreslené, nemažeme cache
    measure_time(lambda: fib_mem(a, {}), 100)
    measure_time(lambda: fib_iter(a), 100)
    measure_time(lambda: fib(a))


if __name__ == "__main__":
    main()
