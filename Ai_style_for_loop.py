print("loop 1 process model prediction:")
predictions_1 = [0.2,0.8,0.91,0.36,0.76]
for prediction1 in predictions_1:
    
    if prediction1 < 0.5:
        continue
    print("positive:",prediction1)

print("loop 2 find first high confidence prediction:")
predictions_2 = [0.21,0.32,0.47,0.83,0.91]
for prediction2 in predictions_2:
    if prediction2 >=0.88:
        print("HIgh:",prediction2)
        break

print("loop 3 process batches:")
batches = [
    [0.1,0.2,0.3],
    [0.8,0.9,0.7],
    [0.4,0.5,0.6]
]

for batch in batches:
    for prediction3 in batch:
        if prediction3 <0.5:
            continue
        print("Accepted:",prediction3)

print("loop 4 stop processing of batch")
batches2 = [
    [0.1,0.2,0.3],
    [0.8,-1,0.7],
    [0.4,0.5,0.6]
]
for batch2 in batches2:
    for value in batch2:
        if value == -1:
            break
        print(value)

print("loop 5 printing bigger than or equal to 0.80:") 
batches3 = [
    [0.1,0.8,0.3],
    [0.9,0.7,0.2],
    [0.4,0.95,0.6]
]
for batch3 in batches3:
    for predict3 in batch3:
        if predict3>=0.80:
            print("bigger than or equal to 0.88 is :",predict3)
    