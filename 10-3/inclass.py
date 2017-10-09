def encrypt_6():
    message = str(input("secret code here:"))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newsent = []
    for letter in message:
        if letter in alphabet:
            letter = alphabet.index(letter) + 6
            letter = alphabet[letter:letter+1]
            newsent.append(letter)
        else:
            newsent.append(letter)
    new = ("".join(newsent))
    return new



encrypt_6()
