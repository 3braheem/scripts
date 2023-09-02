def extended_gcd(p, q):
    ##if p == 0:
    ##    return (q, 0, 1)
    ##else:
     ##   gcd, x, y = extended_gcd(q % p, p)
      ##  return (gcd, y - (q // p) * x, x)
    if p == 0:
        return q, 0, 1
    gcd, x1, y1 = extended_gcd(q % p, p)

    x = y1 - (p//q) * x1
    y = x1

    return gcd, x, y


def mod_inverse(e, phi):
    for d in range(3, phi, 2):
        return d if (d * e) % phi == 1 else None
    raise ValueError("There is no modular inverse.")


def prime_gen():
    p = int(input("Enter a prime number: "))
    q = int(input("Enter a prime number: "))
    return (p * q, (p - 1) * (q - 1))


def keygen(e=3):
    n, phi = prime_gen()
    d = mod_inverse(e, phi)
    #gcd, x, _ = extended_gcd(e, phi)
    #if gcd != 1:
    #    raise ValueError("There is no modular inverse.")
    return (n, e, d)


def process_char(n, key, char):
    original = char
    for _ in range(0, key):
        char = (char * original) % n
    return char


def encrypt(n, e, msg):
    ciphertext = [process_char(n, e, ord(x)) for x in msg]
    return(bytes(ciphertext))


def decrypt(n, d, ciphertext):
    byte_array = [e for e in ciphertext]
    msg = [process_char(n, d, x) for x in byte_array]
    return(bytes(msg).decode("utf-8"))


def main():
    choice = 0
    n, e, d = keygen()
    while choice != 3:
        print("1. Encrypt a Message\n")
        print("2. Decrypt a Message\n")
        print("3. Quit\n")
        choice = int(input("Select a number: "))
        match choice:
            case 1:
                msg = str(input("Write a message to encrypt: "))
                print(f"n = {n}, public_key = {e}")
                res = encrypt(n, e, msg)
                print(f"CIPHERTEXT: {res}")
            case 2:
                ciphertext = bytes(input("Ciphertext to decrypt: "), "utf-8")
                print(f"n = {n}, public_key= {e}")
                res = decrypt(n, d, ciphertext)
                print(f"Message: {res}")
            case 3:
                continue
            case _:
                print("Please enter a valid selection (1-3)\n")
                choice = int(input("Select a number: "))


if __name__ == "__main__":
    main()
