print("Loop 1 basic")
for i in range(5):
    for j in range(3):
        print(i,j)

print("loop 2 with multiplication:")
for i in range(1,4):
    for j in range(1,4):
        print(i*j)

print("loop 3 with break:")
for i in range(3):
    for j in range(5):
        if j ==2:
            break
        print(i,j)

print("loop 4 with continue:")
for i in range(3):
    for j in range(5):
        if j ==2:
            continue
        print(i,j)

print("loop 5 both continue and break:")
for i in range(5):
    if i ==3:
        break
    for j in range(5):
        if j ==2:
            continue
        print(i,j)

print("loop 6 inner break vs outer break:")
for i in range(5):
    for j in range(5):
        if j == 2:
            break
        print("i = ",i,"j = ",j)

print("loop 7 inner break vs outer break:")
for i in range(5):
     if i == 2:
         break
                
     for j in range(5):
       
        print("i = ",i,"j = ",j)
