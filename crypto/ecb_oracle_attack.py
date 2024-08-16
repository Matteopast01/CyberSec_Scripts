from pwn import *
import binascii
from time import time
r = remote("padding.challs.cyberchallenge.it", 9030)
r.recvline()
r.recvline()
r.recvline()
r.recvline()
found_char = b""

#secret is two aes blocks long
for i in range (32):

	#I ask for 31 chars of enctryption, the first byte of the secret is included...and so on.
	payload = b"A" * (31-i)
	r.recvline()
	r.sendline(payload)
	server_response = r.recvline().strip().split()[-1].decode('utf-8')
	server_response = binascii.unhexlify(server_response)
	#last byte of the total encryption (31 mine + 1 of the secret)
	last_byte = server_response[31]
    # I try all the bytes 
	for char in string.printable:
	    byte = char.encode()
	    # i sent 31 bytes + one of the possible byte
	    payload = b"A" * (31-i) + found_char
	    sleep(0.7)
	    payload = payload + byte
	    r.sendline(payload)
	    server_response = r.recvline()
	    server_response = r.recvline().strip().split()[-1].decode('utf-8')
	    server_response = binascii.unhexlify(server_response)
	    """if the last byte of encryption of my payload is equal to the last byte
	     of the total encryption, first byte of the secret is found(and so on....)
	     """ 

	    if server_response[31] == last_byte:
	        found_char += char.encode()
	        print(found_char)
	        break
