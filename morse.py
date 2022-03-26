from gpiozero import LED
from time import sleep
from gpiozero import Button
button = Button(6)
blue = LED(17)
green = LED(22)
red = LED(26)
yellow = LED(11)
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
    elif letter == "b":
        morse(b)
    elif letter == "c":
        morse(c)
    elif letter == "d":
        morse(d)
    elif letter == "e":
        morse(e)
    elif letter == "f":
        morse(f)
    elif letter == "g":
        morse(g)
    elif letter == "h":
        morse(h)
    elif letter == "i":
        morse(i)
    elif letter == "j":
        morse(j)
    elif letter == "k":
        morse(k)
    elif letter == "l":
        morse(l)
    elif letter == "m":
        morse(m)
    elif letter == "n":
        morse(n)
    elif letter == "o":
        morse(o)
    elif letter == "p":
        morse(p)
    elif letter == "q":
        morse(q)
    elif letter == "r":
        morse(r)
    elif letter == "s":
        morse(s)
    elif letter == "t":
        morse(t)
    elif letter == "u":
        morse(u)
    elif letter == "v":
        morse(v)
    elif letter == "w":
        morse(w)
    elif letter == "x":
        morse(x)
    elif letter == "y":
        morse(y)
    elif letter == "z":
        morse(z)

    if letter == " ":
        green.on()
        morse(space)
        green.off()
        sleep(0.5)
    else:
        yellow.on()
        sleep(1)
        yellow.off()
blue.off()
red.on()
