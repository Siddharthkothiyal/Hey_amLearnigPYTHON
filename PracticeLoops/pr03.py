# for i in range(1, 5):
#     print("* "* i, end="")
#     print("\n")


def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

for i in range(1, 20):
        if is_prime(i):
            print("* " * i)