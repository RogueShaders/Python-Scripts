import csv
import os
import requests

os.chdir("Day1")
url = "https://jsonplaceholder.typicode.com/todos/1"

data = requests.get(url).json()

with open("leads.csv", newline="") as file:
    reader = csv.DictReader(file)
    firstLine = next(reader)


print(f"Name: {firstLine['Name']} | TODO: {data["title"]}")
    
