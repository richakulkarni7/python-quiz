
user_name = raw_input("What's your name? ")
score=0

#dictionaries:
print "Hello ",user_name,"!"
qa = {1: 'b', 2: 'a', 3: 'c', 4: 'c', 5: 'd'}
questions = {
	1: "Who was Harry asked to save in the Triwizard Tournament?\na. Hermione\nb. Ron\nc. Gabrielle\nd. Dobby",
	2: "How old were Lily and James when they died?\na. 21\nb. 22\nc. 20\nd. 25",
	3: "Who called Hermione the brightest witch of her age? \na. Molly\nb. Professor Dumbledore\nc. Sirius\nd. Professor Flitwick",
	4: "When did the Battle of Hogwarts take place?\na. May 5\nb. June 5\nc. May 2\nd. June 2",
	5: "Who was the last master of the Elder Wand?\na. Draco\nb. Dumbledore\nc. Snape\nd. Harry"
	}
answers = {}
grade = {
	0: "Troll. Are you sure you aren't a masquerading Muggle? ",
	7: "Dreadful. Being better than a troll isn't something to write home about, really.", 
	14: "Poor, but I suppose you tried.", 
	21: "Acceptable. There is hope.", 
	28: "Exceeds Expectations. Now, now, this is impressive.", 
	35: "Outstanding. Hi, Hermione!" 
	}

#questions
for i in range(1,6):
	print "\nQUESTION ",i, "\n"
	print questions[i]
	a = raw_input ("\nWhat's your answer? ")
	if a==qa[i]:
		score+=7
		answers[i]="Correct"
	else:
		answers[i]="Wrong"
#result
print "\nRESULT: \nFinal score: ", score, "/ 35 \nGrade: ", grade[score]
print "\nANALYSIS: "
for i in range(1,6):
	print "Question", i, ": ", answers[i]
	if answers[i]=="Wrong":
		print "\tCorrect answer: ", qa[i]

