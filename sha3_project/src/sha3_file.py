
import hashlib
import os

def sha3_256_file(file_path):
  hasher = hashlib.sha3_256()
  with open(file_path, 'rb') as f:
    while chunk := f.read(8192):
      hasher.update(chunk)
  return hasher.hexdigest()

file_path = "input.txt"
file_size  = os.path.getsize(file_path) 
hash_value = sha3_256_file(file_path)
hash_bits = len(hash_value) *4

print ("File:", file_path)
print ("Kich thuoc:", file_size, bytes)
print ("SHA3-256 hash:")
print (" ", hash_value)
print (" Do dai:",len(hash_value)," ky tu hexadecimal (", hash_bits, "bit)")
 
