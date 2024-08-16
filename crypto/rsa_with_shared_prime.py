from Crypto.PublicKey import RSA
from sympy import gcd
from Crypto.Util.number import inverse
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

with open("./speedygen/pubkeys/Chloe.pem", "rb") as f:
	data = f.read()
	chloe_public_key = RSA.import_key(data)

with open("./speedygen/pubkeys/Daniel.pem", "rb") as f:
	data = f.read()
	daniel_public_key = RSA.import_key(data)


"""
print("This is chloe_public_key: \n")
print(chloe_public_key.n)
print(chloe_public_key.e)

print("This is Daniel_public_key: \n")
print(daniel_public_key.n)
print(daniel_public_key.e)
"""

shared_prime = gcd(chloe_public_key.n, daniel_public_key.n)
second_prime = daniel_public_key.n/shared_prime

if (shared_prime*second_prime == daniel_public_key.n):
	phi_n = (shared_prime-1)*(second_prime-1)
	daniel_private_key = inverse(int(daniel_public_key.e), int(phi_n))
	with open("./speedygen/messages/Daniel.enc", "rb") as file:
		byte_data = file.read()
		long_encryted_message = bytes_to_long(byte_data)
		long_clear_message = pow(long_encryted_message, daniel_private_key, daniel_public_key.n)
		print(long_to_bytes(long_clear_message))
		


