import math

def recursive_term(prev, x, k):
    return prev * x ** 2 / ((2 * k - 1) * (2 * k))

def cosh_generator(x, epsilon):
    term = 1
    yield term

    k = 1
    while True:
        term = recursive_term(term, x, k)
        if abs(term) < epsilon:
            break
        yield term
        k += 1

def cosh_series(x, epsilon):
    total = 0
    for term in cosh_generator(x, epsilon):
        total += term
    return total


def main():
    x = float(input("Enter x: "))
    epsilon = float(input("Enter epsilon: "))

    approx = cosh_series(x, epsilon)
    exact = math.cosh(x)

    print("Series result:", approx)
    print("math.cosh:", exact)
    print("Difference:", abs(approx - exact))


if __name__ == "__main__":
    main()
