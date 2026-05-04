"""
Zadání

Naprogramujte funkci gcd(a, b), která vrátí GCD (největší společný dělitel) dvou celých čísel a, b.
Výsledkem jee největší celé číslo d, pro které platí, že d dělí a i b beze zbytku.

Např.:
- 24 má dělitele: 1, 2, 3, 4, 6, 8, 12, 24
- 30 má dělitele: 1, 2, 3, 5, 6, 10, 15, 30
Společné dělitele jsou 1, 2, 3, 6 a největší z nich je 6, tedy gcd(24, 30) = 6.

## Eukleidův algoritmus (rekurzivně)
Eukleidův algoritmus je velmi starý (přes 2000 let), ale dodnes používaný postup,
jak GCD najít efektivně pomocí operace modulo % (zbytek po dělení).

### Klíčová myšlenka
Pro a > 0 platí:

    gcd(a, b) = gcd(b % a, a)

kde:
- b % a je zbytek po dělení b číslem a

### Základní případ 
Jakmile dostaneme a == 0, platí:

    gcd(0, b) = |b|



## Úkol
Doplňte funkci gcd(a, b) tak, aby:
- správně fungovala i pro vstupy obsahující 0 a záporná čísla,
- dodržela signaturu funkce,
- můžete použití rekurzivní řešení nebo iterativní, není důležitá efektivita, ale správnost řešení.

Nepoužívejte žádné další knihovny.

Příklady:
- gcd(42, 28)  -> 14
- gcd(28, 42)  -> 14
- gcd(345, 766)-> 1
"""


def gcd(a: int, b: int) -> int:
    """Vrátí GCD (největší společný dělitel) čísel a a b.    """
    a=abs(a)
    b=abs(b)
    while True:
        if a==0:
            return abs(b)
        tmp=a
        a=b%a
        b=tmp
    #if a==0:
    #    return b
    #return gcd(b%a,a)

if __name__ == "__main__":
    print(gcd(0,-4))