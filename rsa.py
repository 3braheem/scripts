def mod_inverse(e, phi):
    m0, x, y = phi, 1, 0
    if phi == 1: return 0

    while (e > 1):
        q = e // phi 
        t = phi
        phi = e % phi
        e, t = t, y
        y = x - q * y
        x = t
    if x < 0: x = x + m0
    return x


def prime_gen():
    p = int(input("Enter a prime number: "))
    q = int(input("Enter a prime number: "))
    return (p * q, (p - 1) * (q - 1))


def keygen(e=65537):
    n, phi = prime_gen()
    d = mod_inverse(e, phi)
    if not d:
        raise ValueError("There is no modular inverse")
    return (n, e, d)


def process_char(n, key, char):
    original = char
    for _ in range(0, key):
        char = (char * original) % n
    return char


def encrypt(n, e, msg):
    ciphertext = [process_char(n, e, ord(x)) for x in msg]
    return(bytes(ciphertext).hex())


def decrypt(n, d, ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
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
                msg = input("Write a message to encrypt: ")
                print(f"n = {n}, public_key = {e}")
                res = encrypt(n, e, msg)
                print(f"CIPHERTEXT: {res}")
            case 2:
                ciphertext = input("Ciphertext to decrypt: ")
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
