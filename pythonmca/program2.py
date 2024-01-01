#Write a Python program to read a file line by line and store it into a list.
with open("prgm2.txt","r") as z:
	content= z.readlines()
print(content)
content_list = [i.strip() for i in content]
print(content)
