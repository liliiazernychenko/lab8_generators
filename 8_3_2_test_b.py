def recursive_term(prev, i):
    return prev * (i + 1) / (i + 2)

def product_generator(n):
    p = 1
    for i in range(1, n + 1):
        p = recursive_term(p, i)
        yield p

def compute_product(n):
    result = 1
    for value in product_generator(n):
        result = value
    return result

def main():
    n = int(input("Enter n: "))
    print("Pn =", compute_product(n))


if __name__ == "__main__":
    main()
