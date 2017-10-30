# Program implementing cube and sphere objects
from COOB import coob
from Spherio import SPhere

def main():
    r_input = int(input("Radius of the sphere: \n"))
    s = SPhere(r_input)
    s.surface_area()
    s.volume()

    s_input = int(input("Side length of the cube: \n"))
    c = coob(s_input)
    c.surface_area()
    c.volume()

main()
