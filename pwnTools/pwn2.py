from pwn import *

r = remote("software-18.challs.olicyber.it", 13001)
r.recvuntil(b"secondi")
r.recvline()
r.recvline()
r.sendline(b'')
r.recv()
while True:
    string_to_manage = r.recv().decode('utf-8').rstrip("\n")
    print(string_to_manage)
    splitted_string = string_to_manage.split()
    dimension = splitted_string[-4][:2]
    argument = splitted_string[-7]
    result = b''

    if dimension == "32":
        result = p32(eval(argument), endianness="little") 
    else:
        result = p64(eval(argument), endianness="little") 
    
    r.send(result)

r.close()
