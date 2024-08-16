from pwn import *
from time import time
r = remote("notadmin.challs.cyberchallenge.it", 9032)
r.recv()
r.sendline(b"1")
r.recv()
r.sendline(b"A"*12)
token = r.recv().split()[3].strip().decode()
third_block = token[32:64]
byte_to_change = hex(bytes.fromhex(third_block)[10]-1)[2:]
third_block = bytes.fromhex(third_block).hex()
third_block = third_block[0:20] + byte_to_change[0] + byte_to_change[1]+ third_block[22:]

while True:
	sleep(1)
	print(r.sendline(b"2"))
	print(r.recv())
	token = os.urandom(16).hex()+ third_block + token[64:]
	token = token.encode()
	print(r.sendline(token))
	print(r.recv())
	token=token.decode()



