

#transfers all letters down 1 and z = 1
file = open("guido_vonRossum_speech.txt", "r")
data = file.read()
string = str(data)
string = string.lower()




string = string.replace('z', '1' )
string = string.replace('y', 'z' )
string = string.replace('x', 'y' )
string = string.replace('w', 'x' )
string = string.replace('v', 'w' )
string = string.replace('u', 'v' )
string = string.replace('t', 'u' )
string = string.replace('t', 'u' )
string = string.replace('s', 't' )
string = string.replace('r', 's' )
string = string.replace('q', 'r' )
string = string.replace('p', 'q' )
string = string.replace('o', 'p' )
string = string.replace('n', 'o' )
string = string.replace('m', 'n' )
string = string.replace('l', 'm' )
string = string.replace('k', 'l' )
string = string.replace('j', 'k' )
string = string.replace('i', 'j' )
string = string.replace('h', 'i' )
string = string.replace('g', 'h' )
string = string.replace('f', 'g' )
string = string.replace('e', 'f' )
string = string.replace('d', 'e' )
string = string.replace('c', 'd' )
string = string.replace('b', 'c' )
string = string.replace('a', 'b' )

print(string)
