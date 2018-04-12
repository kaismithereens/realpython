from random import choice

#vocabulary
noun = ['fossil','horse','animal','sea','judge','life','monkey','breeze','boss','cloud','fog','dog','unicorn','fairy']
verb = ['kisses','dances','climbs','runs','walks','kicks','jingles','bounces','cuddles','hugs','embraces']
adjective = ['furry','balding','incredible','amorous','funny','entertaining','wild','free','hopeful']
preposition = ['against', 'after', 'into', 'over', 'beneath', 'upon', 'for', 'in', 'like', 'within','above']
adverb = ['curiously', 'quickly', 'extravagantly', 'firmly', 'furiously', 'slowly', 'sensously', 'bigly']

def make_poem():
	noun1 = choice(noun)
	noun2 = choice(noun)
	noun3 = choice(noun)
	
	while noun2 == noun1:
		noun2 = choice(noun)
	while noun3 == noun1 or noun3 == noun2:
		noun3 = choice(noun)
	
	verb1 = choice(verb)
	verb2 = choice(verb)
	verb3 = choice(verb)
	
	while verb2 == verb1:
		verb2 = choice(verb)
	while verb3 == verb1 or verb3 == verb2:
		verb3 = choice(verb)
	
	adjective1 = choice(adjective)
	adjective2 = choice(adjective)
	adjective3 = choice(adjective)
	
	while adjective2 == adjective1:
		adjective2 = choice(adjective)
	while adjective3 == adjective1 or adjective3 == adjective2:
		adjective3 = choice(adjective)
	
	preposition1 = choice(preposition)
	preposition2 = choice(preposition)
	
	while preposition2 == preposition1:
		preposition2 = choice(preposition)
	
	adverb1 = choice(adverb)
	
	vowels = 'aeiouAEIOU'

	if adjective1[0] in vowels:
		article1 = "An"
	else:
		article1 = "A"
		
	if adjective3[0] in vowels:
		article3 = "an"
	else:
		article3 = "a"
	
	
	poem = "{} {} {}\n\n".format(article1, adjective1, noun1)
	poem = poem + "{} {} {} {} the {} {}\n".format(article1, adjective1, noun1, verb1, preposition1, adjective2, noun2)
	poem = poem + "{} the {} {}\n".format(adverb1, noun1, verb2)
	poem = poem + "the {} {} {} {} {} {}\n".format(noun2, verb3, preposition2,article3, adjective3, noun3)
	
	return poem

print(make_poem())