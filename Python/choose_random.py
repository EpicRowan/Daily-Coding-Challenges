import os, random
file = open(random.choice(os.listdir("/home/rowan/Dev/Daily Coding Challenges/Python")))
print(file.name)