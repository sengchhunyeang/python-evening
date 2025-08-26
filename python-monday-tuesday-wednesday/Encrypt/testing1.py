import hashlib
password = "chhunyeang123"

# First apply MD5
md5_hash = hashlib.md5(password.encode()).hexdigest()

# Then apply SHA1 on the MD5 result
double_hash = hashlib.sha1(md5_hash.encode()).hexdigest()

print(double_hash)