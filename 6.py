# 7Boom - 1 to 100 don't print /7 or has 7 in it
a = 0
while a <= 100:
    if a % 7 != 0 and '7' not in str(a):
        print(a)
    a = a + 1


