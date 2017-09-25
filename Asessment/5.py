def encrypt_6(message, dict):
    newsent = []
    for letter in message:
        if letter in dict:
            newsent.append(dict[letter])
        else:
            newsent.append(letter)
    print(" ".join(newsent))
dict = {}
dict['z'] = 't'
dict['y'] = 's'
dict['x'] = 'r'
dict['w'] = 'q'
dict['v'] = 'p'
dict['u'] = 'o'
dict['t'] = 'n'
dict['s'] = 'm'
dict['r'] = 'l'
dict['q'] = 'k'
dict['p'] = 'j'
dict['o'] = 'i'
dict['n'] = 'h'
dict['m'] = 'g'
dict['l'] = 'f'
dict['k'] = 'e'
dict['j'] = 'd'
dict['i'] = 'c'
dict['h'] = 'b'
dict['g'] = 'a'
dict['f'] = 'z'
dict['e'] = 'y'
dict['d'] = 'x'
dict['c'] = 'w'
dict['b'] = 'v'
dict['a'] = 'u'




message = str(input("secret code here"))
encrypt_6(message, dict)
