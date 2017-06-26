#!/usr/bin/python3
import time

# Tell me about the clock
print("Clock info: ", time.get_clock_info('time'))

# Tell me the time
print("The time is now: ", time.time())
print("The local time: ", time.localtime())

# Time only runs in one direction
old_monotime = 0;
old_systime = 0;

while True:
    time.sleep(5)
    monotime = time.monotonic()
    systime = time.time() 

    if monotime < old_monotime:
        print("ERROR! monotime is not monotonic!")
    if systime < old_systime:
        print("WARNING! systime has been modified!")

    # time delta
    delta_monotime = monotime - old_monotime
    delta_systime = systime - old_systime

    if delta_monotime != monotime:
        print("monotime delta is: ", delta_monotime)
    if delta_systime != systime:
        print("systime delta is: ", delta_systime)


    print("The monotime is now: ", monotime)
    print("The system time is now: ", systime)

    old_monotime = monotime
    old_systime = systime 


