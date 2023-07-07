import time
# Write a function countdown() that takes in an integer argument 
# and uses a while loop to countdown from that integer to 1, 
# outputting f'{number} SECOND(S)!' in each iteration of the loop. 
# The function should print() "HAPPY NEW YEAR!" after the loop finishes:
def countdown(count):
    i = 0
    while i < count:
        print(f"{count - i} SECOND(S)!")
        i += 1
    
    print("HAPPY NEW YEAR!")

# Write a second function called countdown_with_sleep() 
# that also takes one integer argument for the countdown 
# and makes the loop pause for one second each trip around 
def countdown_with_sleep(count):
    i = 0
    while i < count:
        print(f"{count - i} SECOND(S)!")
        time.sleep(1)
        i += 1
    
    print("HAPPY NEW YEAR!")