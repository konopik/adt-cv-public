#Otevření souboru, použití Dataclass, Deque
from __future__ import annotations
import sys
from dataclasses import dataclass,field
from collections import deque
@dataclass
class Person:
    name:str
    age:int
    friend:Person|None = None

filename:str = input('Filename: ')
Persons:set[Person] = set()
try:
    with open(filename,'r',encoding='utf8') as f:
        next(f) #přeskočit hlavičku souboru
        for line in f:
            args = line.strip().split()
            if len(args) == 2:
                try:
                    name = args[0]
                    age = int(args[1])
                except ValueError:
                    continue
            else:
                continue
            P = Person(name,age)
            Persons.add(P)
except FileNotFoundError:
    sys.exit(0)

dq:deque = deque(maxlen=5)
for P in Persons:
    dq.append(P)

@dataclass(frozen=True)
class User:
    name: str
    email: str
    # Provoznı udaj: nechceme v rovnosti ani v hashi
    last_login: int = field(default=0, compare=False, hash=False, repr=False)
u1 = User("Petr", "p@a.cz", last_login=1)
u2 = User("Petr", "p@a.cz", last_login=999)
u1 == u2
# True
hash(u1) == hash(u2) # True

# Vytvorenı rozptylove tabulky studentu
hash_dict = {}
hash_dict["A16N0123P"] = "Frantisek Vonasek"
hash_dict["A17N0321P"] = "Kateˇrina ˇ Cumackova"
hash_dict["A17P0314P"] = "Tomas Marny"
# Vyhledanı hodnoty podle klıce
key = "A17N0321P"
if key in hash_dict:
    print(f"Student {key} se jmenuje {hash_dict[key]}")
else:
    print(f"Student {key} neni v tabulce.")


#Zásobník - Lifo
#Fronta Fifo

