s = open("Strings_lists_tuples_yzak", 'r')
s = s.read()
s = str(s)
print(s)
def replace(s, o, a):
    s = s.replace(o, a )
    return s


new = replace(s, 'o', 'a')
print(new)
