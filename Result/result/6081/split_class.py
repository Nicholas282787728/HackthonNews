
file_story_class = open('story_class.dat', 'r')

file_story_class0 = open('story_class0.data', 'w')
file_story_class1 = open('story_class1.data', 'w')
file_story_class2 = open('story_class2.data', 'w')
file_story_class3 = open('story_class3.data', 'w')
file_story_class4 = open('story_class4.data', 'w')

for line in file_story_class:
	line = line.strip()

	try:
		story_id, title, text, time, cur_class = line.split('\t')
	except:
		continue
	cur_class = int(cur_class) 

	if cur_class == 0:
		print >> file_story_class0, "%s\t%s\t%s\t%s\t%s\t%s" % (story_id, title, text, time, score, des)
	elif cur_class == 1:
		print >> file_story_class1, "%s\t%s\t%s\t%s\t%s\t%s" % (story_id, title, text, time, score, des)
	elif cur_class == 2:
		print >> file_story_class2, "%s\t%s\t%s\t%s\t%s\t%s" % (story_id, title, text, time, score, des)
	elif cur_class == 3:
		print >> file_story_class3, "%s\t%s\t%s\t%s\t%s\t%s" % (story_id, title, text, time, score, des)
	elif cur_class == 4:
		print >> file_story_class4, "%s\t%s\t%s\t%s\t%s\t%s" % (story_id, title, text, time, score, des)
