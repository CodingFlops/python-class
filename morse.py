from gpiozero import LED
from time import sleep
blue = LED(17)
blue.off()

def morse(code):
    for stuff in code:
        if stuff == ".":
            blue.on()
            sleep(0.5)
            blue.off()
            sleep(0.5)
        else:
            blue.on()
            sleep(1.5)
            blue.off()
            sleep(0.5) 
a = ".-"
b = "-..."
c = "-.-."
d = "-.."
e = "."
f = "..-."
g = "--."
h = "...."
i = ".."
j = ".---"
k = "-.-"
l = ".-.."
m = "--"
n = "-."
o = "---"
p = ".--."
q = "--.-"
r = ".-."
s = "..."
t = "-"
u = "..-"
v = "..-"
w = ".--"
x = "-..-"
y = "-.--"
z = "--.."
space = "......."
sentence = input("type in a sentence ").lower()
for letter in sentence:
    if letter == "a":
        morse(a)
    if letter == "b":
        morse(b)
    if letter == "c":
        morse(c)
    if letter == "d":
        morse(d)
    if letter == "e":
        morse(e)
    if letter == "f":
        morse(f)
    if letter == "g":
        morse(g)
    if letter == "h":
        morse(h)
    if letter == "i":
        morse(i)
    if letter == "j":
        morse(j)
    if letter == "k":
        morse(k)
    if letter == "l":
        morse(l)
    if letter == "m":
        morse(m)
    if letter == "n":
        morse(n)
    if letter == "o":
        morse(o)
    if letter == "p":
        morse(p)
    if letter == "q":
        morse(q)
    if letter == "r":
        morse(r)
    if letter == "s":
        morse(s)
    if letter == "t":
        morse(t)
    if letter == "u":
        morse(u)
    if letter == "v":
        morse(v)
    if letter == "w":
        morse(w)
    if letter == "x":
        morse(x)
    if letter == "y":
        morse(y)
    if letter == "z":
        morse(z)
    if letter == " ":
        morse(space)
