# tento slovník se vám bude pravděpodobně hodit
opposite = {
    "(": ")",
    "{": "}",
    "[": "]",

    ")": "(",
    "}": "{",
    "]": "[",
}

def check_brackets(string: str) -> bool:
    stack = []
    openings = "({["
    closings = ")}]"

    for char in string:
        # Pokud je znak otevírací závorka, přidáme ho na vrchol zásobníku
        if char in openings:
            stack.append(char)
            
        # Pokud je znak zavírací závorka, musíme provést kontrolu
        elif char in closings:
            # Pokud je zásobník prázdný, chybí nám otevírací závorka -> chyba
            if not stack:
                return False
            
            # Vezmeme a rovnou i odstraníme poslední závorku z vrcholu zásobníku
            top_bracket = stack.pop()
            
            # Zkontrolujeme přes dodaný slovník, jestli k sobě pasují
            if top_bracket != opposite[char]:
                return False

    # Na konci musí být zásobník prázdný (všechny páry byly úspěšně uzavřeny).
    # Výraz len(stack) == 0 rovnou vrací True nebo False.
    return len(stack) == 0

def _print_result(string: str, expected: bool) -> None:
    real = check_brackets(string)
    # těch emoji se můžete zbavit, přijde mi ale, že to vizuálně pomáhá
    status = "✅" if real == expected else "❌"
    print(f"{status} {real=!s:<5}   {expected=!s:<5}   {string=}")

def main() -> None:
    # funkci main si můžete uzpůsobit jak chcete,
    # slouží pouze pro vyzkoušení programu, nikoliv hodnocení

    # správné závorky
    _print_result("([{}])", expected=True)
    _print_result("([{([{}])}])", expected=True)
    _print_result("(){}[]", expected=True)
    _print_result("(()()[()()]{}()[()])", expected=True)

    # nesprávné závorky
    _print_result("(}", expected=False)
    _print_result("([{})", expected=False)
    _print_result("([{([{}}])}])", expected=False)
    _print_result("(){}([]", expected=False)
    _print_result("(()())[()()]{}()[()])", expected=False)

    # nějaký text navíc
    _print_result("def check_brackets(string: str) -> bool:", expected=True)
    _print_result("Myslím si, že to je správně! (No počkat...", expected=False)
    s = "Želvy nosí kostnaté struktury (krunýře[1][2]), které je (někdy) brání před dravci[1][3]."
    _print_result(s, expected=True)

if __name__ == "__main__":
    main()