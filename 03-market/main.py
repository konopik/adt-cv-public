from collections import defaultdict
import os
import sys
from dataclasses import dataclass

@dataclass
class Record:
    time: int
    id_customer: int

def load_data(data_path: str, city: str, shop: str, day: str = "1-Mon") -> \
        dict[str, list[Record]] | None:
    """ Funkce načte data z daného souboru a vrátí je jako slovník.
    Klíčem je název checkpointu a hodnotou je list záznamů.

    Args:
        data_path (str): cesta k adresáři se všemi daty
        city (str): název města, které chceme načíst
        shop (str): název obchodu, který chceme načíst
        day (str, optional): Konkrétní den, který chceme načíst. Defaults to "1-Mon".

    Returns:
        dict[str, list[Record]] | None: slovník s načtenými daty nebo None pokud soubor neexistuje
    """

    # pozn. Můžeme použít default dict, nebo použít běžný slovník a při přidání nového záznamu
    # vždy zkontrolovat, zda klíč již existuje, případně inicializovat prázdný list

    #city_data: dict[str, list[Record]] = {}
    city_data: dict[str, list[Record]] = defaultdict(list)

    print("loading", city)

    path=os.path.join(data_path,city,day,shop+".txt")
    with open(path,"r",encoding="utf-8",) as file:
        _=file.readline()
        lines= file.readlines()
        try:
            for line in lines:
                line.strip()
                splitted=line.split(";")
                time,ckpt,cid,price=splitted
                rec = Record(int(time),int(cid))
                city_data[ckpt].append(rec)
        except Exception as e:
            print("sometinkwentwong:{e}")
    return city_data

def get_passed_set(data: dict[str, list[Record]], key_words: list[str]) -> set[int]:
    """Funkce vrátí množinu zákazníků, kteří prošli alespoň jedním z checkpointů s prefixem
    předaných jako key_words. Do funkce tedy nevstupuje celé jméno checkpointu ale pouze
    jeho prefix (např. vege místo vege_1).

    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        key_words (list[str]): prefixové označení checkpointů, které chceme sledovat

    Returns:
        set[int]: Funkce vrací množinu identifikačních čísel zákazníků.
    """
    customers: set[int] = set()

    for key, value in data.items():
        norm_key = key.split("_")[0]
        if norm_key in key_words:
            for rec in value:
                customers.add(rec.id_customer)

    return customers

def filter_data_time(data: dict[str, list[Record]], cond_time: int) -> dict[str, list[Record]]:
    """Funkce vrátí data omezená na záznamy s časem menším nebo rovným než je cond_time.
    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        cond_time (int): časový limit v sekundách
    Returns:
        dict[str, list[Record]]: vrací data omezená na záznamy s časem menším nebo rovným cond_time.
    """
    ret: dict[str, list[Record]] = defaultdict(list)
    for ckpt,records in data.items():
        for record in records:
            if record.time<=cond_time:
                ret[ckpt].append(record)
    return ret

def get_q_size(data: dict[str, list[Record]], seconds: int) -> int:
    """Funkce vrátí velikost fronty v daném čase.
    Velikost fronty je dána počtem zákazníků, kteří prošli některým z checkpointů
    (vege, frui, meat) a ještě neprošli pokladnou.
    """
    #datax=filter_data_time(data,seconds)
    #vmf= len(get_passed_set(datax,["vege"]))+len(get_passed_set(datax,["frui"]))+len(get_passed_set(datax,["meat"]))
    #kasa=len(get_passed_set(datax,["final_crs"]))
    #x=vmf-kasa
    filter_data=filter_data_time(data,seconds)
    before_payment=get_passed_set(filter_data,["frui","vege","meat"])
    paid=get_passed_set(filter_data,["final_crs"])
    v=before_payment.difference(paid)
    return v

def histogram(data: dict[str, list[Record]]) -> None:
    for i in range(24):
        print(f"{i}:00 --- {get_q_size(data,i*60*60)}")

def main(data_path: str) -> None:
    while True:
        city = input("Zadejte město (Plzeň): ")
        shop = input("Zadejte obchod (shop_a): ")

        if city == "":
            city = "Plzeň"
        if shop == "":
            shop = "shop_a"

        data = load_data(data_path, city, shop)
        cust_in=get_passed_set(data,["gate-keeper"])
        cust_out=get_passed_set(data,["final_crs"])
        print(len(cust_in))
        print(len(cust_out))
        if data is None:
            continue

        histogram(data)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path>")
        sys.exit(1)
    main(sys.argv[1])
