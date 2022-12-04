c = input("Encrypted message: ")
n = input("n: ")
e = input("e: ")

# Use https://factordb.com to get the factors of n
p = input("p: ")
q = input("q: ")

phin = (p - 1) * (q - 1)

d = pow(e, -1, phin)
m = pow(c, d, n)
print(bytes.fromhex(hex(m)[2:]).decode())
