# 1-3 number statistics

import statistics

a = ""
mylist = []
while a != "q":
    a = input("Enter a number or q to quit: ")
    if a != "q" and a.isnumeric():
        mylist.append(float(a))
print ("Mean: " + str(statistics.mean(mylist)))
print ("Median: " + str(statistics.median(mylist)))
print ("Standard deviation: " + str(statistics.stdev(mylist)))
