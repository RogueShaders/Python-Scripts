import csv
import os
os.chdir("Day1")

newLeads = [
    {"name": "Jorden", "budget": 700, "email": "jorden694@gmail.com"},
    {"name": "kate", "budget": 1700, "email": "Kate32@gmail.com"},
]

with open("leads.csv", "a") as file:
    for line in newLeads:
        file.write(f"{line['name']},{line['email']},{line['budget']}\n")
