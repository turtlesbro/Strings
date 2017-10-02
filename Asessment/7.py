try:
    text =  open("her-name-is-alice", "r")
    text = text.read()




    def key_sort(text):
        d = {}
        d2 = {}
        word = ''
        for aline in text:
            letter = aline
            if letter!= ' ':
                word = word + letter
            else:
                d[word] = text.count(word)
                word = ''
        key_list = list(d.keys())
        key_list = sorted(d)
        begin = key_list.index("A")
        for i in key_list[begin:]:
            d2[i] = text.count(i)
        return d2

    d = key_sort(text)

    try:
        file = open("write", "w")
        try:
            file.write(str(d))
        finally:
            file.close()
    finally:
        file.close()
except IOError:
    print("This file is not found.")
#dictionary = {}
#def key_sorted(dictionary):
#
#
#
#    return key_list[begin:]

#alice_words_list = key_sorted(dictionary)
#alphabetical_words = {}

#try:
#    file = open("filefilefile.txt", "w")

#    finally:
#        file.close()

