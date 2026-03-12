# 04-26-Complexity: Kontrola duplicitních zákazníků

V předchozím cvičení `03-market` jste implementovali načítání dat z prodejen obchodního řetězce a výpočet délky fronty pomocí množin.

V tomto cvičení využijeme **data z jednoho konkrétního obchodu** a změříme, jaký je rozdíl mezi použitím `list` a `set` při kontrole duplicit zákazníků.

## Datová sada

Použijte stejná data jako v úloze `03-26-market`. V tomto cvičení budeme pracovat vždy s **jedním konkrétním souborem** (např. `cities/output/Plzen/1-Mon/shop_a.txt`).

Data ke stažení:
[[liks]](https://liks.fav.zcu.cz/adt/exam/service/download-data?filename=cities.zip)

## Měřená úloha

Cílem je **najít všechny unikátní zákazníky** v daném souboru.

Každý řádek dat obsahuje informaci o průchodu zákazníka (identifikovaného `id`) určitým checkpointem (`ckpt`). Pro toto cvičení budeme sledovat pouze hodnoty `id` a zjišťovat, kolik různých zákazníků se v souboru vyskytuje.

Soubor se má načíst **jen jednou** do seznamu zákazníků. Obě porovnávané varianty pak musí pracovat nad stejným seznamem, aby se do měření nepletlo opakované čtení souboru.

Nejprve tedy implementujte pomocnou funkci:

```python
def load_customers(shop_path: str) -> list[str]:
    ...
```

1. Sestavte cestu k souboru pomocí `os.path.join(data_path, "output", city, day, f"{shop}.txt")`.
2. Načtěte soubor po řádcích nebo přes `readlines()` (hlavičku přeskočte).
3. Z každého řádku získejte `id` zákazníka.
4. Uložte všechna ID do seznamu `customers`.
5. Tento seznam vraťte a dále používejte v obou měřených variantách.

### Varianta A – `list`

Implementujte funkci, která dostane seznam zákazníků a vrátí seznam unikátních zákazníků.

```python
def check_ckpt_list(customers: list[str]) -> list[str]:
    ...
```

1. Funkce dostane už připravený seznam `customers`.
2. Udržujte **seznam** (`list`) všech dosud nalezených unikátních zákazníků.
3. Pro každého nově přečteného zákazníka ověřte, zda již v seznamu není:
   - pokud není, přidejte jej (`append`)
   - pokud je, nedělejte nic

V těle funkce používejte operaci `if customer not in seen_list`.

### Varianta B – `set`

Stejnou logiku realizujte pomocí `set`:

```python
def check_ckpt_set(customers: list[str]) -> set[str]:
    ...
```

1. Funkce opět dostane stejný seznam `customers`.
2. Namísto seznamu používejte `set` pro ukládání unikátních zákazníků.
3. Každého zákazníka vložte do množiny pomocí `add`. (U množiny není třeba kontrolovat přítomnost, `add` si s duplicitami poradí efektivně samo.)

## Měření času

Implementujte funkci pro měření času pomocí modulu `timeit`:

```python
def measure(func, customers: list[str], n_runs: int = 5) -> float:
    ...
```

Funkce spustí `func(customers)` několikrát za sebou a vrátí celkový čas.

Důležité je, že seznam `customers` musí být načten **před měřením**. Měření tak bude porovnávat pouze práci se strukturami `list` a `set`, ne rychlost disku nebo parsování souboru.

Ve funkci `main`:
1. Načtěte argumenty z příkazové řádky (cesta k datům, město, obchod, den).
2. Zavolejte `experiment`, který:
   - sestaví cestu k souboru,
   - zavolá `load_customers`,
   - vypíše počet načtených záznamů,
   - změří a vypíše časy pro obě varianty.

### Spouštění programu

Program by měl přijímat argumenty pro specifikaci souboru:

```bash
# Základní použití (použije defaultní hodnoty: Plzeň, shop_a, 1-Mon)
python main.py path/to/cities

# Specifikace konkrétního města, obchodu a dne
python main.py path/to/cities Plzeň shop_b 2-Tue
```

## Co porovnávat a diskutovat

- **Rozdíl v čase**: I na jednom souboru byste měli vidět výrazný rozdíl. Operace `in` nad listem je $O(N)$, nad množinou průměrně $O(1)$.
- **Složitost**: Celková složitost pro zpracování $N$ načtených zákazníků:
  - List: $O(N^2)$ (pro každého zákazníka prohledáváme seznam dosud nalezených unikátů).
  - Set: $O(N)$ (pro každého zákazníka provedeme operaci `add` v průměrně konstantním čase).
- **Počet unikátních prvků**: Čím více unikátních zákazníků v souboru je, tím pomalejší bude varianta s listem.

## K zamyšlení

- **Proč je `list` tak pomalý?**
- **Proč je `set` tak rychlý?**

