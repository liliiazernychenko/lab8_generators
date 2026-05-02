def recursive_term(a_k_minus_2, k):
    return (k - 1) / k * a_k_minus_2

def sequence_generator(n):
    a1 = 1
    yield a1

    if n >= 2:
        a2 = 1
        yield a2

    a_k_minus_2 = a1
    a_k_minus_1 = a2 if n >= 2 else 0

    for k in range(3, n + 1):
        a_k = recursive_term(a_k_minus_2, k)
        yield a_k
        a_k_minus_2, a_k_minus_1 = a_k_minus_1, a_k

def compute_sum(n):
    total = 0
    for value in sequence_generator(n):
        total += value
    return total

def main():
    n = int(input("Enter n: "))
    print("Sn =", compute_sum(n))


if __name__ == "__main__":
    main()
