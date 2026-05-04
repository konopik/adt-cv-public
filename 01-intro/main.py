scores = [50, 80, 45, 90, 30, 60]
for i in range(len(scores)):
    if scores[i] < 50:
        scores.pop(i)
print(scores)

