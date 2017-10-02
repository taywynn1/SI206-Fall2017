import re
fhand = open('actual_data.txt')
l = list()
for line in fhand:
	line = line.rstrip()
	numbers = re.findall('([0-9]+)', line)
	if len(numbers) == 0:
		continue
	else:
		for x in range(len(numbers)):
			all_numbers = int(numbers[x])
			l.append(all_numbers)

print("Total:", sum(l))