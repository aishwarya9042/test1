import random
words=['python','apple','chat']
w=random.choice(words);g=set();l=6
while l and set(w)-g:
 print('Word:',' '.join(c if c in g else '_' for c in w))
 x=input('Guess: ').lower()
 if x in w:g.add(x)
 else:l-=1
print('You won!' if not(set(w)-g) else f'Lost! Word was {w}')
