#!/usr/bin/env python3
from pwn import *

exe = ELF("./sw-19")

if args.REMOTE:
	p = remote("software-19.challs.olicyber.it", 13002)
	print(p.recvuntil(b"secondi"))
	print(p.sendline(b''))
	print(p.recv())

	while True:
		response = p.recv()
		print(response)
		function_name = response.decode("utf-8").split("-> ")[1][:-2]
		address = hex(exe.symbols[function_name])
		print(p.sendline(address.encode()))

