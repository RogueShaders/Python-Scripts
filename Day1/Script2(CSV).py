import csv
import os

os.chdir("Day1")

with open("leads.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']} | Email: {row['Email']} | Budget: {row['Budget']}")