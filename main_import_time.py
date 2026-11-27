from os import times
from time import time
import timeit

'''
    TO DO List
    -Have program repeat the process with the correct number in the first position and the other numbers in the other positions
    -Have the program store the guess in a list and then print the list at the end of the program
    '''

def MeasureTime(password,i):
    #Test code for timeit 
    for m in range(4): 
        if i[m] != password[m]:
             return False
    return True

def compare(times,guess): #Compares the time taken to check each character and decides which character is the correct one
    if max(times) == times[0]:
        guess.append("0")
    elif max(times) == times[1]:
        guess.append("1")
    elif max(times) == times[2]:
        guess.append("2")
    elif max(times) == times[3]:
       guess.append("3")
    elif max(times) == times[4]:
        guess.append("4")
    else:
        print("Error")
        print(max(times))
    print(guess)

def time_attack(password):
    times = []
    guess = []
    i = "01234"
    n = 0
    #First Iteration
    while n <= 4:
        #use timit to measure the time taken to check the password
        time = timeit.repeat(lambda: MeasureTime(password,i), repeat=1000, number=1000)
        #print(min(times))
        times.append(min(time))
        #print(min(time))
        #print(i)
        i = i[1:] + i[0] #move the first character to the end of the string
        n += 1
    compare(times,guess)

   #Second Iteration
    times = [] #Reset times list for the next iteration
    i = "01234" #reset i
    n = 0 #reset n
    while n <= 4:
        l = "".join(guess) + i #We know the first character. Append to beginning of i to check the 2nd character
        print(l)
        #use timit to measure the time taken to check the password
        time = timeit.repeat(lambda: MeasureTime(password,l), repeat=1000, number=1000)
        times.append(min(time))
        print(min(time))
        i = i[1:] + i[0] #move the first character to the end of the string
        n += 1
    compare(times,guess)
    print(guess)

    #Third Iteration
    times = [] #Reset times list for the next iteration
    i = "01234" #reset i
    n = 0 #reset n
    while n <= 4:
        l = "".join(guess) + i #We know the first character. Append to beginning of i to check the 2nd character
        print(l)
        #use timit to measure the time taken to check the password
        time = timeit.repeat(lambda: MeasureTime(password,l), repeat=1000, number=1000)
        times.append(min(time))
        print(min(time))
        i = i[1:] + i[0] #move the first character to the end of the string
        n += 1
    compare(times,guess)
    print(guess)

    #Third Iteration
    times = [] #Reset times list for the next iteration
    i = "01234" #reset i
    n = 0 #reset n
    while n <= 4:
        l = "".join(guess) + i #We know the first character. Append to beginning of i to check the 2nd character
        print(l)
        #use timit to measure the time taken to check the password
        time = timeit.repeat(lambda: MeasureTime(password,l), repeat=1000, number=1000)
        times.append(min(time))
        print(min(time))
        i = i[1:] + i[0] #move the first character to the end of the string
        n += 1
    compare(times,guess)
    print(guess)
 
password = input("Enter a password made of numbers between 0 and 4: ")
time_attack(password)

'''
        #Now that the algorithm has found the first character of the password, start the process again with the new character added to the guess
        n = 0
        while n <= 4:
                #use timit to measure the time taken to check the password
                times = timeit.repeat(lambda: MeasureTime(password,i), repeat=1000, number=1000)
                print(min(times))
                guess.append(min(times))
                print(i)
                i = i[2:] + i[1] #move the second character to the end of the string
                n += 1
        '''
    
    #i = 0
    # while i < 10000:
    #     #Check all zeros
    #     #start = time.perf_counter()
    #     start0 = time.perf_counter_ns()
    #     if "0" == password:
    #         #end = time.perf_counter()
    #         end0 = time.perf_counter_ns()
    #         guess["0"] += end0 - start0
    #     else:
    #         end0 = time.perf_counter_ns()
    #         guess["0"] += end0 - start0
        

    #     #Check all ones
    #     start1 = time.perf_counter_ns()
    #     if "1" == password:
    #         end1 = time.perf_counter_ns()
    #         guess["1"] += end1 - start1
    #     else:
    #         end1 = time.perf_counter_ns()
    #         guess["1"] += end1 - start1

    #     #Check all twos
    #     start2 = time.perf_counter_ns()
    #     if "2" == password:
    #         end2 = time.perf_counter_ns()
    #         guess["2"] += end2 - start2
    #     else:
    #         end2 = time.perf_counter_ns()
    #         guess["2"] += end2 - start2
        
    #     #Check all threes
    #     start3 = time.perf_counter_ns()
    #     if "3" == password:
    #         end3 = time.perf_counter_ns()
    #         guess["3"] += end3 - start3
    #     else:
    #         end3 = time.perf_counter_ns()
    #         guess["3"] += end3 - start3
        
    #     #Check all fours
    #     start4 = time.perf_counter_ns()
    #     if "4" == password:
    #         end4 = time.perf_counter_ns()
    #         guess["4"] += end4 - start4
    #     else:
    #         end4 = time.perf_counter_ns()
    #         guess["4"] += end4 - start4
    #     i += 1

    # print(guess["0"])
    # print(guess["1"])
    # print(guess["2"])
    # print(guess["3"])   
    # print(guess["4"])


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
