print("loop 1 skip invalid valiues:")
batches = [
    [23,54,28,64,23],
    [123,432,456,54,24],
    [54,23,99,34,23]
] 
for batch in batches:
    for value in batch:
        if value <30 or value>100:
            continue
        print(value)

print("loop 2 stop current batch:")
batches2 = [
    [28,54,25,64,23],
    [123,432,456,54,23],
    [54,23,99,34,23]
] 
for batch2 in batches2:
    for value2 in batch2:
        if value2<40:
            break
    print(value2)


print("loop 3 skip all batches:")
batches3 = [
    [28,54,25,64,23],
    [],
    [54,23,99,34,23],
    [],
    [23,34,765,87,76]
] 
for batch3 in batches3:
    
    if not batch3:
        continue
    print(batch3)
    
    for i in batch3:
        print(i)

print("loop 4 multiple conditions:")
batches4 = [
    [0.1,0.2,0.3],
    [0.8,0.9,0.7],
    [0.4,0.5,0.6]
]

for batch4 in batches4:
    for score in batch4:
        if score<=0.2 :
            continue
        if score >=0.8:
            print("very high score:",score)
            break
        print("accepted:",score)

print("loop 5 searching target :")
dataset = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
target = 50
for row in dataset:
    for value in row:
        if value==target:
            print("found:",target)
            break

print("loop 6 controle flow pattern")
batches5 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
found = False
for batch5 in batches5:
    for score5 in batch5:
        if score5>80:
            print("found:",score5)
            found = True
            break
    if found:
        break
        