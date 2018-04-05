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

#figure definitions
fig = plt.figure()

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
    #print plot after every day
    ax = plt.subplot(5, 10, iteration+1)
    ax.plot(Matrix)
    ax.set_xlim(0,50)
    ax.set_ylim(25,75)
    ax.set_title(iteration)
    #iterate days after everyone has given their dollar
    iteration +=1
    count = 0

#print plt object
plt.show()

#printing completed iterations and resulting matrix
print("\nCompleted Iterations:", iteration)
print("Result Matrix:")
print(Matrix)

#printing sorted result table from high to low-
counter = collections.Counter(Matrix)
print("\n[Sorted Result Table]")
print("Amount" + "  | " + "Frequency")
print("===================")
for key, value in sorted(counter.items(), reverse=True):
    print(key, "\t|\t", value)


