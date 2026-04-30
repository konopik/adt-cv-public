def nasob(x:int) -> int:
    return x*2
print(f"Soucin je: {nasob(5)}")

scores = [50, 80, 45, 90, 30, 60]
try:
    for i in range(len(scores)):
        if scores[i] < 50:
            scores.pop(i)
    print(scores)
except IndexError:
    print("IndexError: Nelze odstranit prvek z pole během iterace.")

