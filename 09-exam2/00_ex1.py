
"""
Zadání:
    - Následující program simuluje stav bankovního účtu.
    - Účet má:
        -  majitele,
        -  zůstatek,
        -  denní úrokovou sazbu -- denní sazba nám usnadní výpočty úroků.
    - Účet umožňuje
        - vkladat peníze,
        - vybrat peníze a
        - vypočítat úroky.
    - V simulaci pro zjednodušení předpokládejme, že každý měsíc má 30 dní.
    - Konkrétní zadání vaší simulace, naleznete ve funkci answer_query(...).

    - Implementujte chybějící části kódu a opravte případné chyby.
    - Dodržte signaturu funkcí, neměňte:
        - jména funkcí
        - argumenty a jejich typy
        - návratové typy

    - Držte se jednoduchých řešení
        - Nepoužívejte žádné další knihovny, než ty, které znáte ze cvičení.
        
    - Body: 15 bodů.
"""

from dataclasses import dataclass


@dataclass
class BankAccount:
    """Datová struktura účtu.
        Attributes:
            owner (str): Jméno majitele účtu.
            balance (float): Aktuální zůstatek na účtu.
            daily_interest_rate (float): Denní úroková sazba v procentech (např. 5 pro 5% denně).
    """
    
    owner: str
    balance: float = 0.0
    daily_interest_rate: float = 0.0
    current_date: int = 1


def deposit(account: BankAccount, amount: float) -> bool:
    """Vklad na účet. Vrací True pokud proběhl, jinak False."""
    if amount>0:
        account.balance += amount
        return True
    return False

def withdraw(account: BankAccount, amount: float) -> bool:
    """Výběr z účtu. Vrací True pokud proběhl, jinak False."""
    if (amount>0) and ((account.balance- amount)>=0):
            account.balance -= amount
            return True
    return False


def apply_interest(account: BankAccount) -> None:
    """Připíše denní úrok k aktuálnímu zůstatku."""
    #if account.daily_interest_rate>1:
    #    account.balance=account.balance*(account.daily_interest_rate)
    #if account.daily_interest_rate<1:
    #    account.balance=account.balance*(1+account.daily_interest_rate)
    account.balance=account.balance+(account.balance*(account.daily_interest_rate/100))

def show_balance(account: BankAccount) -> str:
    return f"{account.current_date}: {account.balance:.2f}"


def simulate_scenario_a(account: BankAccount, days: int) -> float:
    """Simulace:

    - každý 15. den v měsíci: +5000
    - každý den: -300 (pokud je dost peněz)
    - na konci každého dne: připíšeme úrok

    Transakce v jednom dni jdou v tomto pořadí: vklad -> výběr -> úrok.
    """
    for day in range(1,days+1):
        if day%30==15:
            deposit(account,5000)
        withdraw(account,300)
        apply_interest(account)
        print(show_balance(account))
        account.current_date+=1
    return account.balance


def answer_query() -> float:
    """
    Returns:
        float: Odpověď na otázku:  Zůstatek účtu po 90 dnech.
    """

    """TODO Simulujte následující scénář:
    Kája si založil účet v bance s denní úrokovou sazbou 0.1 %. Je mu 20 let a na účet si vložil 25000 Kč.
    Na účtu se provádí pravidelné transakce. Pokud je jich více během dne, provedou se v pořadí níže uvedeném: 
        - Každý 15. den v měsíci si na účet ukládá výplatu ze své brigády ve výši 5000 Kč.
        - Každý den si z účtu bere 300 Kč na jídlo a zábavu.
        - Na konci každého dne mu na účet připisují úroky -- použijte metodu apply_interest().
        - Kolik peněz bude mít Kája na svém účtu po 90 dnech?
    """

    account = BankAccount("Kája Kovář", balance=25000, daily_interest_rate=0.1)
    return simulate_scenario_a(account, 90)


if __name__ == "__main__":
    answer_query()