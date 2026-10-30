print("loop 1 filter invalid scores")
scores = [0.91,-1,0.72,1.40,0.88,-5,0.63]
for score in scores:
    if score <0 or score>1:
        continue
    print(score)

print("loop 2 stop after finding target value:")
scores_2 = [0.91,0.1,0.72,1.40,0.88,0.55,0.63]
for score_2 in scores_2:
    if score_2 >=0.60:
        print("target found:",score)

    print("checking:",score_2)


