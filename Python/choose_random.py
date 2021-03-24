import os, random
import subprocess

file = open(random.choice(os.listdir("/home/rowan/Dev/Daily Coding Challenges/Python")))
os.system(f"subl {file.name}")