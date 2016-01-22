

#print text

#tokens = text.split(' ')
#print tokens

# Problems:
# 1. Casing not normalized.
# 2. End of line removal


#tokens = text.split(' ')

#print tokens

# Problems now:
# Punctuation not removed.

import string
from collections import Counter

text = open('carroll-alice.txt', 'r').read()
text = text.replace('\n', ' ')
exclude = set(string.punctuation)
s = ''.join(ch for ch in text if ch not in exclude)
#print s

tokens = s.split(' ')

results = Counter(tokens)

f = open('results.csv','w')

for word,count in results.most_common():
	print word,count
	f.write("{0},{1}\n".format(word,count))

f.close()

#print results


