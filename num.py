# SACH CODE
# If any EOF error occurs this program will take n=8 as default
x = 0
y = 0
try:
    n = int(input("n: "))
except EOFError:
    n = 8
for i in range(1, n):
        if i % 4 == 1:
            x = x + (i * 10)
        if i % 4 == 2:
            y = y + (i * 10)
        if i % 4 == 3:
            x = x - (i * 10)
        if i % 4 == 0:
            y = y - (i * 10)
print('X:',x, ' Y:',y)


