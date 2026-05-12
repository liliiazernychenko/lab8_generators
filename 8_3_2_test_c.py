def determinant(n, x):
    if n == 0:
        return 1

    if n == 1:
        return 1 + x**2

    d0 = 1
    d1 = 1 + x**2

    for _ in range(2, n + 1):
        d2 = (1 + x**2) * d1 - x**2 * d0
        d0 = d1
        d1 = d2

    return d1


def main():
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))

    print("Determinant =", determinant(n, x))


if __name__ == "__main__":
    main()
