import csv
with open("co53.csv") as f:
	data=csv.reader(f)
	for i in data:
		print(i)


