import sys
import csv 

d1 = dict()

with open(sys.argv[1], 'r') as my_file:
	for line in my_file:
		for word in line.split():
			# print(word)
			if word in d1:
				d1[word] = d1[word] + 1
			else:
				d1[word] = 1
	print(d1)

out_file = open("translatoe.csv", "w")

writer = csv.writer(out_file)

for key, value in d1.items():

    writer.writerow([key, value])

out_file.close()


