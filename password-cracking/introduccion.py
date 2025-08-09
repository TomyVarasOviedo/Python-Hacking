import hashlib

md5password = hashlib.md5()
md5password.update(b"12345")
print(md5password.hexdigest())
print(len(md5password.hexdigest()))

sha1password = hashlib.sha1(b"12345")
print(sha1password.hexdigest())
print(len(sha1password.hexdigest()))
