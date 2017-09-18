pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
pirate['madam'] ='proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['the'] = "th’"
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'
sentence = input('Write a sentence: ')
newsent = []
word = sentence.split()
for i in range(len(word)):
    if word[i-1] in pirate:
        newsent.append(pirate[word[-1]])
    else:
        newsent.append(word[i-1])

print(" ".join(newsent))
