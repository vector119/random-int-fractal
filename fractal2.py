"""Program to generate a fractal by the following algorithm:
    1. Choose a regular polygon of your choice and plot it.
    2. Now consider any arbitrary point P of your choice on the plane.
    3. Construct an indexed list of set of random integers within the interval [1,n * (n-1)]
       where n is the number of sides. Map each index to an unique corner of the polygon.
    4. Generate a random integer within the same interval.
    5. Check the index of the set in which the integer lies.
    6. Now, starting from P, proceed towards the corresponding corner and plot a point at
       (n-1)th part of the way from the corner's position.
    7. Finally substitute this new point for P.
    8. Repeat the steps 4 through 7 as many times as you want.
    """

from random import randint as rint

from matplotlib import pyplot as plt
from numpy import arange, pi, exp, real, imag


def urt(n):  # return nth roots of unity
    return exp(2j * pi / n * arange(n))


n = int(input('enter the value of n: '))  # enter the number of sides

l = tuple(urt(n))  # store the output of urt(n) as tuple


def poly(n):  # plot, thus construct a regular unit polygon of side n
    for i in l:
        plt.plot(real(i), imag(i), marker='.', markerfacecolor='green', markersize=1)


poly(n)

fl = []  # initialize list for holding tuples of set of possible random values
k = 1  # for use in the following for loop
for i in range(0, n):  # populate fl with tuples of set of possible values that can be randomly generated
    k0 = k
    fl.append(tuple(range(n * i + k, n * i + k + n - 1)))
    k -= 1

print("set of values for " + str(n) + ": ", fl)

if n%10 == 1:
    suffix = "st"
elif n%10 == 2:
    suffix = "nd"
elif n%10 == 3:
    suffix = "rd"
else:
    suffix = "th"

print(str(n) + suffix + " roots of unity: ", l)

x = float(input("enter abscissa: "))  # enter the abscissa of a random point of user choice
y = float(input("enter ordinate: "))  # enter the ordinate of a random point of user choice
plt.plot(x, y, 'ro')  # plot the point chosen by the user

m = int(input("enter the number of iterations you want: "))

# main loop for iterating the process to generate a fractal
for i in range(0, m):
    d = rint(1, n * (n - 1))
    for z in range(0, n):
        if d in fl[z]:
            plt.plot(((x + real(l[z])) / (n - 1)), ((y + imag(l[z])) / (n - 1)), marker='.', markerfacecolor='green',
                     markersize=10)
            x = ((x + real(l[z])) / (n - 1))
            y = ((y + imag(l[z])) / (n - 1))
            break
        else:
            continue

plt.show()
