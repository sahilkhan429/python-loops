print("loop 1 with continue:")
index = 0
scores = [1,2,3,4,5]
while index < len(scores):
    score = scores[index]
    index+=1
    if score<3:
        continue
    print(score)

print("loop 2 with break:")
index = 0
scores = [1,2,3,4,5]
while index < len(scores):
    score = scores[index]
    if score >=5:
        print("high score:",score)
        break
    print(score)
    index +=1

