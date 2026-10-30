print("loop 1 with break:")
dataset = [
    [0.12,0.34,0.45,0.56],
    [0.78,0.98,0.90,0.56],
    [0.67,0.55,0.23,0.24]
]
target = 0.90
for row in dataset:
    for value in row:
        if value == target:
            print("found:",value)
            break

