
# https://www.ascii-code.com/
# A upper https://www.ascii-code.com/65
# a lower https://www.ascii-code.com/97
# https://www.w3schools.com/python/python_strings_methods.asp
# https://www.digitalocean.com/community/tutorials/python-ord-chr

# test with "dzxp dectyr" = "some string" and encryption key = 11

def get_encryption_key():
    # TODO
    # input a number called Encryption Key, must be integer > 0
    # if not correct number, ask again
    # return an int > 0
    while True:
        raw = input("Encryption Key: ")
        if raw.isdigit():
            key = int(raw)
            if key > 0:
                return key


def get_encrypted_text():
    # TODO
    # input a given line of encrypted text
    # if empty, ask again
    # return a string
    while True:
        s = input("Text: ")
        if s.strip() != "":
            return s


def decrypt(key, s):
    # receives Encryption Key of type int, and s of type string
    # where key is the encryption key
    # s is the encrypted text
    # TODO
    # decrypt the text and return it
    new_s = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            offset = ord('a')
            shifted = (ord(ch) - offset - key) % 26 + offset
            new_s += chr(shifted)
        elif 'A' <= ch <= 'Z':
            offset = ord('A')
            shifted = (ord(ch) - offset - key) % 26 + offset
            new_s += chr(shifted)
        else:
            new_s += ch
    return new_s


def main():
    # do not change below code
    enkey = get_encryption_key()
    encrypted = get_encrypted_text()
    decrypted = decrypt(enkey, encrypted)
    print(f"DECRYPTED: {decrypted}")

if __name__ == "__main__":
    main()
