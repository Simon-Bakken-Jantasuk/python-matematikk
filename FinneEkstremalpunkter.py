## Finne ekstremalpunktene til andregrads polynom.

def f(x):
    return x**2+10*x+25

def fderivert(x):
    return 2*x+10

# while loop
x = -10
while x < 10
    if fderivert(x) == 0:
        print(x, f(x))
    x = x + 1

# Alternativ til while loop; så kan det lages en for loop.
for x in range(-10,11):
    if fderivert(x) == 0:
        print(x, f(x))
    x = x + 1
# Mye finere...
