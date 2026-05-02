def recursive_term(prev, x, k):
    return -prev * x * (k - 1) / k

def sequence_generator(x, n):
    x1 = -x
    yield x1
    prev = x1

    for k in range(2, n + 1):
        current = recursive_term(prev, x, k)
        yield current
        prev = current

def main():
    x = float(input("Enter x: "))
    n = int(input("Enter n: "))

    print("Sequence elements:")
    for term in sequence_generator(x, n):
        print(term)

if __name__ == "__main__":
    main()
