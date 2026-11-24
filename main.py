import time

passwords = []
i = 0
while i < 4: 
    num = int(input("Enter a number between 0 and 4: "))
    passwords.append(num)
    i += 1

guess = [0,1,2,3,4]
for j in passwords: 
    for k in guess: 
        start = time.perf_counter()
        if j == k:
            end = time.perf_counter()
        print("Time taken for each position ", end - start)