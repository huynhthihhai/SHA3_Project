
import hashlib

def sha3_256_hash(message):
  hasher = hashlib.sha3_256()
  hasher.update(message.encode('utf-8'))
  return hasher.hexdigest()

input_string = "Hello World"
hash_value = sha3_256_hash(input_string)
print (f"SHA3-256 hash of '{input_string}':")
print (f" {hash_value}")
print (f" Do dai: {len(hash_value)} ky tu hexadecimal")

