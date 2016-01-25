import re

senti = open('OpinionFinder_Lexicon.tff','r').read().splitlines()

#print senti

line = senti[0]
tokens = line.split(' ')

print tokens

word = tokens[2]

matches = re.match(r'word1=(.+)', word)

term = matches.group(1)

score = 0

if tokens[0] == 'type=weaksubj':
	score = 1
elif tokens[0] == 'type=strongsubj':
	score = 3

polarity = 0

if tokens[5] == 'priorpolarity=negative':
	polarity = -1
elif tokens[5] == 'priorpolarity=positive':
	polarity = 1

score = polarity * score

print term, score