import time

password = input("Enter a password made of numbers between 0 and 4: ")

def time_attack():
    guess = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    }
# passwords = []
# i = 0
# while i < 4:
#     num = int(input("Enter a number between 0 and 4: "))
#     passwords.append(num)
#     i += 1
# pw = ''.join(str(x) for x in passwords)
# guess = [0,1,2,3,4]
# for j in passwords:
#     for k in guess:
#         start = time.perf_counter()
#         if j == k:
#             end = time.perf_counter()
#             #print("correct")  
#             print("C = Time taken: ", end - start) 
#         else:
#             end = time.perf_counter()  
#             print("F = Time taken: ", end - start)
