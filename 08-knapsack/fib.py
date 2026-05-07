import functools
import math
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

<<<<<<< HEAD
    if n not in lookup:
        lookup[n] = fib_mem(n - 1,lookup) + fib_mem(n - 2,lookup)

    return lookup[n]

def fastest_algorith(n:int)->int:
    if n <= 1:
        return n
    res = [0,1]
    for i in range(2,n+1):
        res.append(res[i-1]+res[i-2])
    return res[n]

=======
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b
>>>>>>> 647550344f5f6c5bb77e147253782b678edc7ade

def main() -> None:
    #lookup: dict[int, int] = {}

<<<<<<< HEAD
    a = 200 # to je hned
=======
    # a = 20 # to je hned
>>>>>>> 647550344f5f6c5bb77e147253782b678edc7ade
    # a = 30 # to už chvilku trvá
    a = 90 # za jak dlouho se asi dočkáme? Nikdy

<<<<<<< HEAD
    measure_time(lambda: fib_cache(a), 1)
    measure_time(lambda: fib_mem(a, {}), 1)
    #measure_time(lambda: fib(a))
    print(fastest_algorith(a))
    measure_time(lambda: fastest_algorith(a),1)
=======
    measure_time(lambda: fib_cache(a), 100)
    measure_time(lambda: fib_mem(a, {}), 100)
    measure_time(lambda: fib_iter2(a), 100)
    #measure_time(lambda: fib(a))
    
    print(fib_cache(a))
>>>>>>> 647550344f5f6c5bb77e147253782b678edc7ade


if __name__ == "__main__":
    main()
