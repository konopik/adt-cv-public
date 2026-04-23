data = 3,7,6,11,5,5,8,9
prev = 0

for value in data: 
    if value != prev:
        print(value/(value - prev))
    prev = value