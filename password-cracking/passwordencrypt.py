import hashlib


def main():
    password = input("Palabra: ")
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    print(f"MD5: {md5_hash} => {len(md5_hash)} caracteres")
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    print(f"SHA1: {sha1_hash} => {len(sha1_hash)} caracteres")
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"SHA256: {sha256_hash} => {len(sha256_hash)} caracteres")
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()
    print(f"SHA512: {sha512_hash} => {len(sha512_hash)} caracteres")


if __name__ == "__main__":
    main()
