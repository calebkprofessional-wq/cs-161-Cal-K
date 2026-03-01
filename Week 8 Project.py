import time
#1.____________________________________________
word1 = input("\nEnter a phrase: ")
word2 = input("\nEnter the phrase in uppercase: ")
#sees if the lower versions of both phrases are the same and if word2 is uppercase
if word1.lower() == word2.lower() and word2.isupper():
    print("\nStop shouting please!")

#2.____________________________________________
vowels = ['a', 'e', 'i', 'o', 'u']
word3 = input("\nEnter a word: ")
total_vowels = 0
#iterates through word3
for i in word3:
    #if i is in vowels, add one to the total of vowels and remove i from the vowels list
    if i in vowels:
        total_vowels += 1
        vowels.remove(i)

print(f"\n{word3} has {total_vowels} different vowels")

#3.____________________________________________
word4 = input("\nEnter a string: ")
word5 = input("\nEnter a string: ")
if word4 == word5:
    print("\nNeither word comes before the other!")
elif word4 > word5:
    print(f"\n{word5} comes before {word4}")
else:
    print(f"\n{word4} comes before {word5}")

#4.___________________________________________
#enter two strings until they are the same
while True:
    email1 = input("\nEnter your email: ")
    email2 = input("\nEnter your email again: ")
    if email1 == email2:
        print("\nThank you!")
        break
    else:
        print("\nEmail 1 does not match email 2.")
        continue

#5.___________________________________________
start = time.perf_counter_ns()
total = 1
#iterative
for i in range(1,4):
    total*=i
print(f"\nthe factorial of 3 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

start = time.perf_counter_ns()
#recursive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
total = factorial(3)
print(f"\nthe factorial of 3 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

#and again and again...
start = time.perf_counter_ns()
total = 1
for i in range(1,11):
    total*=i
print(f"\nthe factorial of 10 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

start = time.perf_counter_ns()
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
total = factorial(10)
print(f"\nthe factorial of 10 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

start = time.perf_counter_ns()
total = 1
for i in range(1,26):
    total*=i
print(f"\nthe factorial of 25 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

start = time.perf_counter_ns()
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
total = factorial(25)
print(f"\nthe factorial of 25 is {total}")
stop = time.perf_counter_ns()
print(stop - start)

print("The recursive version of the factorial function seems to be quicker. Also, as the number we compute gets larger, so does the time it takes to run the program.")