"""Program to generate a fractal
    The Algorithm is mentioned in Algorithm.md"""

from random import randint as rint

from matplotlib import pyplot as plt
from numpy import arange, pi, exp, real, imag


def urt(n):  # return nth roots of unity
    return exp(2j * pi / n * arange(n))


n = int(input('enter the value of n: \n'))  # enter the number of sides

l = tuple(urt(n))  # store the output of urt(n) as tuple


def poly(n):  # plot, thus construct a regular unit polygon of n number of sides
    for i in l:
        plt.plot(real(i), imag(i), marker='.', markerfacecolor='green', markersize=1)


poly(n)

print(" ")

if n % 10 == 1:
    suffix = "st"
elif n % 10 == 2:
    suffix = "nd"
elif n % 10 == 3:
    suffix = "rd"
else:
    suffix = "th"

print(str(n) + suffix + " roots of unity: ", l, "\n")

x = float(input("enter abscissa: "))  # enter the abscissa of a random point of user choice
y = float(input("\nenter ordinate: "))  # enter the ordinate of a random point of user choice
plt.plot(x, y, 'ro')  # plot the point chosen by the user

m = int(input("\nenter the number of iterations you want: "))

print('\n', str(m) + " iterations underway. Generating figure. Please wait...\n")
# main loop for iterating the process to generate a fractal
for i in range(0, m):
    d = rint(1, n * (n - 1))
    z = int(d / (n - 1)) - 1
    plt.plot(((x + real(l[z])) / (n - 1)), ((y + imag(l[z])) / (n - 1)), marker='.', markerfacecolor='green',
             markersize=10)
    x = ((x + real(l[z])) / (n - 1))
    y = ((y + imag(l[z])) / (n - 1))

plt.show()

print("Program finished!")
print("Exiting...")
