# Halveringsmetoden
"""
En metode for å numerisk løse en likning f(x) = 0
Hvor f er en kontinuerlig funksjon definert over et intervall.
[x_0,x_1] hvor f(x_0) og f(x_1) har motsatte fortegn.
1. Du må ha 2 forskjellige x-verdier
2. Kalkuler midpunkt c = (x_0 + x_1)/2
"""


## Finner nullpunkter ved Halveringsmetoden
def f(x):
    return x**3-x**2-2

x_0 = 1
x_1 = 2

x = (x_0 + x_1)/2

y = f(x)

# while loop
while round(y, 10) != 0:
    if y < 0:
        x_0 = x
    else:
        x_1 = x

    x = (x_0 + x_1)/2
    y = f(x)

print(x,y)
