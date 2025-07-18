import random
import time
import threading

max_range = 9999999
total_randoms = 0
total_seconds = 0
should_exit = False
needed_number = random.randint(1, max_range)

def count_seconds():
    global total_seconds
    global should_exit 
    while 1:
        time.sleep(1)
        total_seconds = total_seconds + 1
        if should_exit:
            exit()

def print_value(value):
    global total_randoms
    global should_exit
    if value != needed_number:
        print(value)
    else:
        print()
        print(value)
        print("Nice.")
        print()
        print("Total randomizations: " + str(total_randoms))
        print("Total seconds taken: " + str(total_seconds))
        should_exit = True
        exit()

def get_random_number():
    global total_randoms
    total_randoms = total_randoms + 1
    return random.randint(1, max_range)

def main():
    while 1:
        number = get_random_number()
        print_value(number)
        time.sleep(0.000000001) # Limits speed as to not runaway.

thread1 = threading.Thread(target=main) 
thread2 = threading.Thread(target=count_seconds)

thread1.start()
thread2.start()

thread1.join()   
thread2.join()

