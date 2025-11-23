import csv
import os

try:
    file = open("leads.csv")
except FileNotFoundError:
    os.chdir("Day1")
finally:
    file = open("leads.csv")

reader = csv.reader(file)

for line in reader:
    print("Name: " + str(line[0]) +" | Email: "+ str(line[1])+ " | Budget: " + str(line[2]))