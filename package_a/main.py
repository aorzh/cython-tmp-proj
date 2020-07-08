from package_b.fib import fib
from package_b.simple import Shrubbery


def main():
    # plain python func which import func and class from pyx
    n = 10
    h = 5
    w = 4
    fib(n)
    shrubbery = Shrubbery(w, h)
    shrubbery.describe()


if __name__ == '__main__':
    main()
