
print("BASIC LOOP CODE:")
print("loop 1:")
for i in range(5):
    print(i)
print("loop 2:")
for i in range(1,6):
    print(i)
print("loop 3:")
for i in range(0,11,2):
    print(i)
print("LOOP OVER A LIST:")
print("loop 4:")
numbers = [10,20,30,40,50]
for number in numbers:
    print(number)

print("LOOP OVER STRINGS:")
print("loop 5:")
text = "Ai"
for ch in text:
    print(ch)
print("loop 6 with break:")
for number in range(10):
    
    if number==5:
        break
    print(number)
print("loop 7 with continue:")
for number in range(10):
    
    if number==5:
        continue
    print(number)

print("loop 8 printing numbers 1 to 20 but skipping all even numbers:")
for i in range(1,20):
    if i %2==0:
        continue
    print(i)

print("loop 9 printing numbers 1 to 100 but numbers will be stop when = 37")
for i in range (1,100):
    if i ==37:
        break
    print(i)


