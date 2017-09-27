import re

fhand = open('mbox-short.txt')
#I accumulated parts a-c into lists to avoid having all the empty lists in parts a and c
from_list = list()
name_list = list()
number_list = list()
for line in fhand:
	line = line.rstrip()
	#Part a of the assignment
	from_results = re.findall('From .+', line)
	if len(from_results) == 0:
		continue
	lines = from_results[0]
	from_list.append(lines)
	#Part b of the assignment
	number_results = re.findall('From .+\s.+\s.+\s ([0-9:].+)', line)
	numbers = number_results[0]
	number_list.append(numbers)
	#Part c of the assignment 
	results =  re.findall('From (\S+)@', line)
	if len(results) == 0:
		continue
	name = results[0]
	name_list.append(name)
#print(name_list)
#print(from_list)
#print(number_list)
