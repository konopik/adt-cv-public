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
#b
def fib_mem(n: int, lookup: dict[int, int]) -> int:
    if n <= 1:
        return n

    if n not in lookup:
        lookup[n] = fib_mem(n - 1,lookup) + fib_mem(n - 2,lookup)

    return lookup[n]


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
    lookup: dict[int, int] = {}

    a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    # a = 40 # za jak dlouho se asi dočkáme?

    measure_time(lambda: fib_cache(a), 100)
    print(fib_cache(a))
    measure_time(lambda: fib_mem(a, {}), 100)
    print(fib_mem(a, lookup))
    #measure_time(lambda: fib(a))
    measure_time(lambda: fib_fast(a), 100)
    print(fib_fast(a))

if __name__ == "__main__":
    main()
