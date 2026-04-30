from collections import defaultdict
import os
import sys
from dataclasses import dataclass

@dataclass
class Record:
    time: int
    id_cust: int

def load_data(data_path: str, city: str, shop: str, day: str = "1-Mon") -> dict[str, list[Record]] | None:
    """Funkce načte data z daného souboru a vrátí je jako slovník.
    Klíčem je název checkpointu a hodnotou je list záznamů.

    Args:
        data_path (str): cesta k adresáři se všemi daty
        city (str): název města, které chceme načíst
        shop (str): název obchodu, který chceme načíst
        day (str, optional): Konkrétní den, který chceme načíst. Defaults to "1-Mon".

    Returns:
        dict[str, list[Record]]|None: slovník s načtenými daty nebo None pokud soubor neexistuje
    """

    # pozn. Můžeme použít default dict, nebo použít běžný slovník a při přidání nového záznamu
    # vždy zkontrolovat, zda klíč již existuje, případně inicializovat prázdný list

    city_data: dict[str, list[Record]] = dict()
    # city_data: dict[str, list[Record]] = defaultdict(list)

    print("loading", city)

    shop_path = os.path.join(data_path, city, day, f"{shop}.txt")
    if not os.path.exists(shop_path):
        print("soubor neexistuje", shop_path)
        return None

    with open(shop_path, "r", encoding="utf8") as fd:
        _ = fd.readline()  # skip header

        lines = fd.readlines()
        for line in lines:
            line = line.replace("\n", "")  # remove newline character

            spl = line.split(";")
            try:
                r = Record(int(spl[0]), int(spl[2]))
                key = spl[1]
                if key not in city_data:
                    city_data[key] = list()
                city_data[key].append(r)
            except ValueError:
                print("chyba v souboru ValueError neocekavana hodnota", shop_path, "\n", line)
                continue
            except IndexError:
                print("chyba v souboru IndexError neocekavany pocet hodnot", shop_path, "\n", line)
                continue

    return city_data

def get_passed_set(data: dict[str, list[Record]], key_words: list[str]) -> set[int]:
    """Funkce vrátí množinu zákazníků, kteří prošli alespoň jedním z checkpointů s prefixem předaných jako key_words.
    Do funkce tedy nevstupuje celé jméno checkpointu ale pouze jeho prefix (např. vege místo vege_1).

    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        key_words (list[str]): prefixové označení checkpointů, které chceme sledovat (např. vege, frui, meat)

    Returns:
        set[int]: Funkce vrací množinu identifikačních čísel zákazníků.
    """
    customers: set[int] = set()

    for k, d in data.items():
        # Díky prefixování klíče checkpointu (vege_1, vege_2, ...) můžeme snadno zjistit, zda checkpoint obsahuje některé z klíčových slov.
        # Díky tomu můžeme např. snadno posčítat zákazníky, kteří prošli jakýmkoli vege_X (X je identifikátor pokladny pro zeleninu)

        d_ckpt_gen = k.split("_")[0]  # vege_1 -> vege
        if d_ckpt_gen in key_words:
            for r in d:
                customers.add(r.id_cust)

    return customers

def filter_data_time(data: dict[str, list[Record]], cond_time: int) -> dict[str, list[Record]]:
    ret: dict[str, list[Record]] = defaultdict(list)
    """Funkce vrátí data omezená na záznamy s časem menším nebo rovným než je cond_time.

    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        cond_time (int): časový limit v sekundách

    Returns:
        dict[str, list[Record]]: vrací data omezená na záznamy s časem menším nebo rovným než je cond_time.
    """

    for k, d in data.items():
        for r in d:
            if r.time <= cond_time:
                ret[k].append(r)
            else:
                # Protože jsou data seřazená podle času, můžeme v momentě, kdy narazíme na záznam s vyšším časem, cyklus ukončit.
                break

    return ret

def get_q_size(data: dict[str, list[Record]], seconds: int) -> int:
    """Funkce vrátí velikost fronty v daném čase.
    Velikost fronty je dána počtem zákazníků, kteří prošli některým z checkpointů (vege, frui, meat) a ještě neprošli pokladnou.
    """

    data_time = filter_data_time(data, seconds)

    # Zákazníci, kteří prošli některým z checkpointů (vege, frui, meat)
    # Tito zákazníci jsou potenciálně ve frontě před pokladnou
    passed_set = get_passed_set(data_time, ["vege", "frui", "meat"])

    # Zákazníci, kteří již prošli pokladnou
    # Tito zákazníci již frontu opustili
    checkout_set = get_passed_set(data_time, ["final-crs"])

    # Velikost fronty je rozdíl mezi množinou zákazníků, kteří přišli a množinou zákazníků, kteří odešli
    return len(passed_set - checkout_set)

def histogram(data: dict[str, list[Record]]):
    for i in range(8, 20):
        print(f"{i}:00 {get_q_size(data, i * 3600)}")

def find_most_congested_checkpoint(
    data: dict[str, list[Record]],
    allowed_queues: tuple[str, ...] = ("vege", "frui", "meat"),
) -> tuple[int, str, int]:
    """Najde frontu a hodinu s nejvíce příchody (viz README).

    Returns:
        (best_time_seconds, best_checkpoint, best_queue_size)

    Poznámka:
        - Vyhodnocujte pouze fronty: vege, frui, meat.
        - Frontu final-crs nevyhodnocujte.
        - Příchody počítejte jako počet řádků (záznamů).
    """
    best_time=8
    best_ckpt=""
    best_size=0
    for cp,rec in data.items():
        for record in rec:
            pass
    for i in range(9, 20):
        for y in allowed_queues:
            print(get_passed_set(data,y))
            if len(filter_data_time(data,i))<len(filter_data_time(data,i-1)):
                best_time=i

                get_passed_set(data,y)



    return best_time, best_ckpt, best_size


def main(data_path: str):

    while True:
        city = input("Zadejte město (Plzeň): ")
        shop = input("Zadejte obchod (shop_a): ")

        if city == "":
            city = "Plzeň"
        if shop == "":
            shop = "shop_a"

        data = load_data(data_path, city, shop)
        if data is None:
            continue

        # Histogram ve zkouškovém zadání nepoužívejte.
        # Vaším úkolem je doplnit find_most_congested_checkpoint(...).
        best_time, best_ckpt, best_size = find_most_congested_checkpoint(data)

        if best_time < 0 or best_ckpt == "" or best_size < 0:
            print("TODO: Doplňte funkci find_most_congested_checkpoint(...) podle README.")
            continue

        hh = best_time // 3600
        print("Nejvíce příchodů do fronty:")
        print(f"Fronta: {best_ckpt}")
        print(f"Počet příchodů (záznamů): {best_size}")
        print(f"Hodina: {hh:02d}:00")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path>")
        sys.exit(1)
    main(sys.argv[1])