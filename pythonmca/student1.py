import csv
with open("student.csv","r") as d:
	data=csv.reader(d)
        for i in data:
		print(i)
	

