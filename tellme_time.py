#!/usr/bin/python3
import time

# Tell me about the clock
print("Clock info: ", time.get_clock_info('time'))

# Tell me the time
print("The time is now: ", time.time())
print("The local time: ", time.localtime())

# Time only runs in one direction
old_monotime = 0
old_systime = 0
output = ""

column_names = [ "Monotime", "System Time", "Mono Delta", "System Delta" ] 
column_gen = ["time.monotonic()", "time.time()", "monotime - old_monotime", "systime - old_systime"]
border = "||"
column_sep = "||"

print("||  Monotime  ||  System Time  ||  Mono Delta  ||  System Delta  ||")
print("===================================================================")

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

    output += "|| " + str(monotime) + " || " + str(systime) + " || " + str(delta_monotime) + " || " + str(delta_systime) + " ||"

    #if delta_monotime != monotime:
        #print("monotime delta is: ", delta_monotime)
    #if delta_systime != systime:
        #print("systime delta is: ", delta_systime)

    print(output)
    output = ""
    #print("The monotime is now: ", monotime)
    #print("The system time is now: ", systime)

    old_monotime = monotime
    old_systime = systime 


