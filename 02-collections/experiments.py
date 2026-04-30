from dataclasses import dataclass
from collections import defaultdict

data = list(range(10))

print(data[1::2])

@dataclass(frozen=True)
class Student:
    name: str
    os_cislo: str
    
student = Student(name="John Doe", os_cislo="A01N001")

print(hash(student))

student2 = Student(name="John Doe", os_cislo="A01N001")

print(hash(student2))
print()

slovnik : defaultdict[str, list[str]] = defaultdict(lambda : ["Ahoj"])

slovnik["matematika"].append("Martin")
slovnik["matematika"].append("Jana")
slovnik["angličtina"].append("Martin")

print(slovnik)


print(slovnik["chemie"])
print("chemie" in slovnik)


