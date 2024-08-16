import binascii
from Crypto.Cipher import AES
hex_to_iterate = ["a","b" ,"c","d","e","f","0","1","2","3","4","5","6","7","8","9"]

c2= "78c670cb67a9e5773d696dc96b78c4e0"
p2= b"very unbreakable"
"""
invented_c1 = "c5aaaaaaaaaaaaaaaaaaaaaaaaaad49e"

for elem1 in hex_to_iterate:
	for elem2 in hex_to_iterate:
		for elem3 in hex_to_iterate:
			for elem4 in hex_to_iterate:
				partial_key = "796e395242334c723433784a4b32"
				partial_key = partial_key + elem1 +elem2+ elem3+elem4

				aes = AES.new(bytes.fromhex(partial_key), AES.MODE_CBC, bytes.fromhex(invented_c1))
				decrypted = aes.decrypt(bytes.fromhex(c2))
				l= []
				l.append(partial_key)
				l.append(decrypted)
				print(l)
			


"""
p1=b"AES with CBC is "
real_key="yn9RB3Lr43xJK2tp"
aes = AES.new(real_key.encode(), AES.MODE_ECB)
decrypted = aes.decrypt(bytes.fromhex(c2))
c1 = bytes([a^b for (a,b) in zip (decrypted,p2)])
IV_XOR_P1 = aes.decrypt(c1)
IV = bytes([a^b for (a,b) in zip (IV_XOR_P1,p1)])
print(IV)


