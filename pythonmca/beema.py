import csv
field("roll no","name",age")
sdict={"roll no":22,"name":beema,"age":"22"}
with open("dept.csv","w") as d
writer=csv.dictwriter(d,filename=field)
writer.writeheader()
writer.write rows(sdict)
