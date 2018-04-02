#
# Authors: Victor Kim 
#          Brian Powell
# EE381
# Chaw-Long Chu
# 

import random as rand
import matplotlib.pyplot as plt
import numpy as np
import collections

#static variables
people = 50
amount = 50
iteration = 0
count = 0

#initialize matrix of 50 people to $50 each
Matrix = [amount for x in range(people)]

#Print initial matrix
print("Initial Matrix:")
print(Matrix)

#Days
while (iteration < 50):
    #People
    for count in range(people):
        Matrix[count] -= 1
        Matrix[rand.randint(0,49)] += 1
        count +=1
    #iterate days after everyone has given their dollar
    iteration +=1
    count = 0

#printing completed iterations and resulting matrix
print("\nCompleted Iterations:", iteration)
print("Result Matrix:")
print(Matrix)

#printing sorted result table from high to low
counter = collections.Counter(Matrix)
print("\n[Sorted Result Table]")
print("Amount" + "  | " + "Frequency")
print("===================")
for key, value in sorted(counter.items(), reverse=True):
    print(key, "\t|\t", value)

#creating and showing histogram
plt.title('Money Distribution After 50 Days')
plt.xlabel("Money Owned")
plt.ylabel("Number of People")
plt.hist(Matrix, bins=range(min(Matrix), max(Matrix) + 1, 1),edgecolor='black')
plt.show()

