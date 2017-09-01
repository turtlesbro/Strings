file = open("guido_vonRossum_speech.txt", "r")
data = file.read()
string = str(data)
string = string.lower()
i = True

while i == True:
    remove = input('what letter do you want removed? 0 to stop')
    if remove == '0':
        i = False
        remove = ''
    string = string.replace(remove, "")
print(string)
