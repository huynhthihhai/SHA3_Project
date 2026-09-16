import hashlib

def count_diff_bits(hash1, hash2):
  bytes1 = bytes.fromhex(hash1)
  bytes2 = bytes.fromhex(hash2)
  diff = 0
  for b1, b2 in zip (bytes1, bytes2):
    diff += bin (b1^b2).count('1')
  return diff

print ("TEST 1: TINH XAC DINH")
input_str = "Hello World"
hash1 = hashlib.sha3_256(input_str.encode()).hexdigest()
hash2 = hashlib.sha3_256(input_str.encode()).hexdigest()
print("Input: ",input_str)
print ("Hash lan 1:", hash1)
print ("Hash lan 2:", hash2)
ketqua = "GIONG NHAU " if hash1 == hash2 else "KHAC NHAU"
print("Ket qua:", ketqua)
print ()

print ("TEST 2: DO DAI DAU RA CO DINH")
for inp in ["A", "Hello World", "A"*1000,"Mot file co kich thuoc hang tram MB"]:
  h = hashlib.sha3_256(inp.encode()).hexdigest()
  print ("Input", len(inp), "ky tu -> Hash", len(h), "ky tu hex (", len(h)*4, "bit)")
print ()

print ("TEST 3: HIEU UNG  Avalanche")
input1 = "Hello World"
input2 = "Hello world"
 
h1 = hashlib.sha3_256(input1.encode()).hexdigest()
h2 = hashlib.sha3_256(input2.encode()).hexdigest()

diff = count_diff_bits(h1, h2)
percent = diff/256*100

print ("Input 1:", input1)
print ("Input 2:", input2)
print ("Hash 1: ", h1)
print ("Hash 2: ", h2)
print ("So bit khac nhau:", diff, "/256 (", round(percent, 2), "%)")
print ()

input3 = "Hello World"
input4 = "Hello World!"

h3 = hashlib.sha3_256(input3.encode()).hexdigest()
h4 = hashlib.sha3_256(input4.encode()).hexdigest()

diff2 = count_diff_bits(h3,h4)
percent = diff2/256*100

print ("Input 3:", input3)
print ("Input 4:", input4)
print ("Hash 3:", h3)
print ("Hash 4:", h4)
print ("So bit khac nhau:", diff2, "/256 (", round(percent, 2), "%)")
print () 

print ("TEST 4: TINH TOAN VEN")

original = "Du lieu quan trong"
modified = "Du lieu quan trong!"

ho = hashlib.sha3_256(original.encode()).hexdigest()
hm = hashlib.sha3_256(modified.encode()).hexdigest()

print ("Du lieu goc:", original)
print ("Hash goc:", ho)
print ("Du lieu sua:", modified)
print ("Hash sua:",hm)
ketqua2 = "TOAN VEN" if ho ==hm else "DA BI THAY DOI"
print ("Ket qua:", ketqua2)
print ()


