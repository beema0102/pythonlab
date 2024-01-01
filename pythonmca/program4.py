#Write a Python program to read specific columns of a given CSV file and print the content of the columns.
import csv
with open("co34.csv") as f:
	data = csv.DictReader(f)
print("ID Department Name")
print("---------------------------------")
for row in data:
		print(row['department_id'], row['department_name'])
