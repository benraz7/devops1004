a = "Moshe"
b = "David"
c = a + " " + b
i = {"name": "aviel"}
d = f"{i['name']} {b}"  # f=format
e = "%s %s" % (a, b)
f = "{} {}".format(a, b)
g = 'aviel'
h = "aviel \"buskila\""
j = 5
k = a + str(j)

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(k)