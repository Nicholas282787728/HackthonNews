from numpy import *

file_class = open('./model_theta.dat', 'r')
file_story = open('./table4', 'r')

file_out = open('story_class.dat', 'w')

for line_class in file_class:
	line_story = file_story.readline()
	line_class=line_class.strip()
	line_story=line_story.strip()

	# assign class
	possibilities = line_class.split('\t')

	max_possi = 0.0
	assign_class = -1
	for i in range(len(possibilities)):
		try:
			tmp = float(possibilities[i])
		except:
			print 'error: ', possibilities[i]
		possibilities[i] = tmp
		if possibilities[i] > max_possi:
			max_possi = possibilities[i]
			assign_class = i

	print >> file_out, "%s %d" % (line_story, assign_class)

file_open=open('story_class.dat', 'r')
table=[]
for line in file_open:
    table.append(line)
table=asarray(table)
print table[0]
table=table.reshape(table.shape[0],5)

