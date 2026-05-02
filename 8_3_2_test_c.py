def recursive_det(prev, x):
    return prev * (1 + x ** 2)

def diagonal_generator(n, x):
    for _ in range(n):
        yield 1 + x ** 2

def determinant(n, x):
    det = 1
    for value in diagonal_generator(n, x):
        det = recursive_det(det, x)
    return det

def main():
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))

    print("Determinant =", determinant(n, x))


if __name__ == "__main__":
    main()
