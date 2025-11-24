# Q1: Function to check if a number is prime with AI-generated test cases
def is_prime(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        # Check only odd numbers up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# ---------- Test Cases ----------
if __name__ == "__main__":
    tests = [0, 1, 2, 3, 4, 17, 18, -5, 97, 100]
    print("Prime Number Test Cases:")
    for t in tests:
        print(f"{t} -> {is_prime(t)}")