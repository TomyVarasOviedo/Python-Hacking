import hashlib
import urllib.request


def main():
    hash_to_crack = input("Enter the hash to crack: ")
    passwordlist = urllib.request.urlopen(
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou.txt"
    )

    for password in passwordlist.split("\n"):
        z = hashlib.md5(password.encode("utf-8")).hexdigest()
        if z == hash_to_crack:
            print(f"Password found: {password}")
            return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
