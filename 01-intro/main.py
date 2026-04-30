names = ["Alice", "Bob", "Charlie", "David", "Eve"]
pairs = []

for i in range(len(names)):
    if i + 1 < len(names):
        pairs.append(names[i] + " - " + names[i+1])

print(pairs)


