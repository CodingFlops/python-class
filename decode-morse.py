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

#decode = "..-." # f
#decode = ".-.." # l
#decode = "..-..-.." # fl
decode = "..-..-..---" # flo

print("String to decode:", decode)
while len(decode)>0:
    print("DEBUG",  decode)
    print(decode[:len(f)])
    if len(f)<=len(decode) and decode[:len(f)] == f:
        print("f")
        decode = decode[len(f):]
    elif len(l)<=len(decode) and decode[:len(l)] == l:
        print("l")
        decode = decode[len(l):]
    elif len(o)<=len(decode) and decode[:len(o)] == o:
        print("o")
        decode = decode[len(o):]
    
