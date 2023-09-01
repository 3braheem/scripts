def extended_gcd(p, q):
    if p == 0:
        return (q, 0, 1)
    else:
        gcd, x, y = extended_gcd(q % p, p)
        return (gcd, y - (q // p) * x, x)


def prime_gen():
    p = int(input("Enter a prime number: "))
    q = int(input("Enter a prime number: "))
    return (p * q, (p - 1) * (q - 1))


def keygen(max, phi, pub=65537):
    _, phi = prime_gen()
    gcd, x, _ = extended_gcd(pub, phi)
    if gcd != 1:
        raise ValueError("There is no modular inverse.")
    return (max, pub, x % phi)


def process_char(max, key, char):
    original = char
    for _ in range(1, key):
        char = (char * original) % max
    return char


def encrypt(max, pub, msg):
    msg = bytes(msg, "utf-8")
    return map(lambda x: process_char(max, pub, x), msg)


def decrypt(max, priv, msg):
    return map(lambda x: process_char(max, priv, x), msg)


def main():
    choice = 0
    max, phi = prime_gen()
    n, e, d = keygen(max, phi)
    while choice != 3:
        print("1. Encrypt a Message\n")
        print("2. Decrypt a Message\n")
        print("3. Quit\n")
        choice = int(input("Select a number: "))
        match choice:
            case 1:
                #some

            case 2:
                #some

            case _:
                print("Please enter a valid selection (1-3)\n")
                choice = int(input("Select a number: "))


if __name__ == "__main__":
    main()
