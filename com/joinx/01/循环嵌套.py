from math import fabs

i=2
while i<100:
    j=2
    while j<=(i/j):
        if not(i%j):break
        j=j+1
    if (j>i/j):print(i)
    i=i+1
print('good bye')
a=-1
print(abs(a)==1)
print(fabs(a)==1)