# write code to create a list of 10 random numbers between 1 and 100
# and then print the list

import random

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

