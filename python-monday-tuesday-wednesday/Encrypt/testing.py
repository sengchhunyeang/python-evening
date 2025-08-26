import hashlib

# The hash we want to crack
target_hash = "67566701d6d774067fb23a3de492810bd66c97f8"

# Example list of possible passwords
wordlist = ["password", "123456", "EP031POUNh", "admin", "qwerty"]

def sha1_of_md5(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha1_hash = hashlib.sha1(md5_hash.encode()).hexdigest()
    return sha1_hash

# Try each password in the list
for word in wordlist:
    if sha1_of_md5(word) == target_hash:
        print(f"Password found: {word}")
        break
else:
    print("Password not found in the wordlist.")
