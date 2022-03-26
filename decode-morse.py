a = ".- "
b = "-... "
c = "-.-. "
d = "-.. "
e = ". "
f = "..-. "
g = "--. "
h = ".... "
i = ".. "
j = ".--- "
k = "-.- "
l = ".-.. "
m = "-- "
n = "-. "
o = "--- "
p = ".--. "
q = "--.- "
r = ".-. "
s = "... "
t = "- "
u = "..- "
v = "..- "
w = ".-- "
x = "-..- "
y = "-.-- "
z = "--.. "

#decode = "..-. "   # f
#decode += ".-.. "  # l
#decode += "--- "   # o
#decode += ".-. "   # r
#decode += ".. "    # i
#decode += ".- "    # a
#decode += "-. "    # n

decode = "..-. .-.. --- .-. .. .- -. "

def decodeMorse(decode):
    if len(a)<=len(decode) and decode[:len(a)] == a:
        print("a", end='')
        decode = decode[len(a):]
    elif len(b)<=len(decode) and decode[:len(b)] == b:
        print("b", end='')
        decode = decode[len(b):]
    elif len(c)<=len(decode) and decode[:len(c)] == c:
        print("c", end='')
        decode = decode[len(c):]
    elif len(d)<=len(decode) and decode[:len(d)] == d:
        print("d", end='')
        decode = decode[len(d):]
    elif len(e)<=len(decode) and decode[:len(e)] == e:
        print("e", end='')
        decode = decode[len(e):]
    elif len(f)<=len(decode) and decode[:len(f)] == f:
        print("f", end='')
        decode = decode[len(f):]
    elif len(g)<=len(decode) and decode[:len(g)] == g:
        print("g", end='')
        decode = decode[len(g):]
    elif len(h)<=len(decode) and decode[:len(h)] == h:
        print("h", end='')
        decode = decode[len(h):]
    elif len(i)<=len(decode) and decode[:len(i)] == i:
        print("i", end='')
        decode = decode[len(i):]
    elif len(j)<=len(decode) and decode[:len(j)] == j:
        print("j", end='')
        decode = decode[len(j):]
    elif len(k)<=len(decode) and decode[:len(k)] == k:
        print("k", end='')
        decode = decode[len(k):]
    elif len(l)<=len(decode) and decode[:len(l)] == l:
        print("l", end='')
        decode = decode[len(l):]
    elif len(m)<=len(decode) and decode[:len(m)] == m:
        print("m", end='')
        decode = decode[len(m):]
    elif len(n)<=len(decode) and decode[:len(n)] == n:
        print("n", end='')
        decode = decode[len(n):]
    elif len(o)<=len(decode) and decode[:len(o)] == o:
        print("o", end='')
        decode = decode[len(o):]
    elif len(p)<=len(decode) and decode[:len(p)] == p:
        print("p", end='')
        decode = decode[len(p):]
    elif len(q)<=len(decode) and decode[:len(q)] == q:
        print("q", end='')
        decode = decode[len(q):]
    elif len(r)<=len(decode) and decode[:len(r)] == r:
        print("r", end='')
        decode = decode[len(r):]
    elif len(s)<=len(decode) and decode[:len(s)] == s:
        print("s", end='')
        decode = decode[len(s):]
    elif len(t)<=len(decode) and decode[:len(t)] == t:
        print("t", end='')
        decode = decode[len(t):]
    elif len(u)<=len(decode) and decode[:len(u)] == u:
        print("u", end='')
        decode = decode[len(u):]
    elif len(v)<=len(decode) and decode[:len(v)] == v:
        print("v", end='')
        decode = decode[len(v):]
    elif len(w)<=len(decode) and decode[:len(w)] == w:
        print("w", end='')
        decode = decode[len(w):]
    elif len(x)<=len(decode) and decode[:len(x)] == x:
        print("x", end='')
        decode = decode[len(x):]
    elif len(y)<=len(decode) and decode[:len(y)] == y:
        print("y", end='')
        decode = decode[len(y):]
    elif len(z)<=len(decode) and decode[:len(z)] == z:
        print("z", end='')
        decode = decode[len(z):]
    return decode

print("String to decode: ", decode)
print("         decoded: ", end='')

while len(decode)>0:
    # print("DEBUG",  decode)
    decode = decodeMorse(decode)
print()
