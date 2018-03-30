#@author: victorkim

import random as rand
import matplotlib.pyplot as plt
import numpy as np

people = 50
amount = 50
iteration = 0
count = 0

Matrix = [amount for x in range(people)]

#Print initial matrix
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

print("\nIteration", iteration)
print(Matrix)

plt.hist(Matrix, bins=range(min(Matrix), max(Matrix) + 1, 1))
plt.title("Result after 50 days")
plt.xlabel("Number of People")
plt.ylabel("Money Owned")