print("loop 1:")
count = 0
while count<5:
    print(count)
    count+=1

print("loop 2 with while + break")
count = 0
while True:
    print(count)
    if count==4:
        break
    count+=1

print("loop 3 with while + continue")

count = 0
while count < 10:
    count+=1
    
    if count%2==0:
       continue
    print(count)