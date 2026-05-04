from dataclasses import dataclass, field

@dataclass
class Transaction:
    action: str
    amount: float
    new_balance: float  # Nový parametr pro zůstatek po transakci

@dataclass
class InvestmentAccount:
    balance: float
    history: list[Transaction] = field(default_factory=list)

    interest: float = 0.006
    dividend: float = 0.02
    deposit: float = 10_000.0

def _add_transaction(account: InvestmentAccount, action: str, amount: float) -> None:
    """
    Přidá do účtu finance (amount) a zapíše novou transakci.
    """
    # 1. Zvýšíme zůstatek na účtu o danou částku
    account.balance += amount
    
    # 2. Vytvoříme záznam, kde rovnou předáme i ten nový zůstatek
    new_txn = Transaction(action=action, amount=amount, new_balance=account.balance)
    
    # 3. Přidáme transakci do historie
    account.history.append(new_txn)

def _simulate_interest_monthly(account: InvestmentAccount) -> None:
    """ Zhodnocení zůstatku úrokovou sazbou ."""
    # Použijeme hodnotu interest přímo z účtu
    interest_amount = account.balance * account.interest
    _add_transaction(account, "Interest", interest_amount)

def _simulate_dividend_monthly(account: InvestmentAccount, month: int) -> None:
    """ Přičtení dividendy na aktuální zůstatek ."""
    # Každý 3. měsíc (když je zbytek po dělení třemi roven 0)
    if month % 3 == 0:
        dividend_amount = account.balance * account.dividend
        _add_transaction(account, "Dividend", dividend_amount)

def _simulate_deposit_monthly(account: InvestmentAccount) -> None:
    """ Přičte termínovaný vklad ."""
    # Použijeme hodnotu deposit přímo z účtu
    _add_transaction(account, "Deposit", account.deposit)

def _simulate_month(account: InvestmentAccount, month: int) -> None:
    """ Provede simulaci jednoho měsíce na účtu. Tuto funkci neměňte. """
    _simulate_interest_monthly(account)
    _simulate_dividend_monthly(account, month)
    _simulate_deposit_monthly(account)

def simulate_investment_account(account: InvestmentAccount, num_months: int) -> None:
    """ Spustí celou simulaci na zadaný počet měsíců ."""
    # Projdeme všechny měsíce (od 0 do num_months - 1)
    for month in range(num_months):
        # Zavoláme předpřipravenou funkci, která se postará o všechny tři operace
        _simulate_month(account, month)


def main() -> None:
    # funkci main si můžete uzpůsobit jak chcete,
    # slouží pouze pro vyzkoušení programu, nikoliv hodnocení
    account = InvestmentAccount(balance=0.0)
    simulate_investment_account(account, num_months=12)

    print("Historie transakcí:")
    for tr in account.history:
        line = f"{tr.action:12} | {tr.amount:10,.2f} kč | balanc: {tr.new_balance:10,.2f} kč"
        line = line.replace(",", " ") # prostě nahradím oddělovače tisíců...
        print(line)

    line = f"\nPeníze po simulaci: {account.balance:,.2f} kč"
    line = line.replace(",", " ") # prostě nahradím oddělovače tisíců...
    print(line)

if __name__ == "__main__":
    main()