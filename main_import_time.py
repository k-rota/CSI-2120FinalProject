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
