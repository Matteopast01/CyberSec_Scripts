from pwn import *
import sys
import math
from functools import reduce
sys.set_int_max_str_digits(1000000000)


 
def gcd_list(numbers):
    return reduce(math.gcd, numbers)

r = remote("oracle.challs.cyberchallenge.it", 9041)
r.recvuntil(b"flag: ")
flag = int(r.recvline().rstrip().decode('utf-8').strip(" "))
r.recv()
e=65537

encryptions = {}

for i in range (10):

	r.sendline(b"1")
	r.recv()
	i_input = str(i+2).encode()
	r.sendline(i_input)
	r.recvuntil(b": ")
	number = int(r.recvline().rstrip().decode('utf-8').strip(" "))
	encryptions[(i+2)**e] = number
	r.recv()






numbers = [ chiave -valore for chiave, valore in encryptions.items()] 




n = gcd_list(numbers)
#print(f"The GCD is {n}")


r.sendline(b"1")
r.recv()
r.sendline(b"2")
r.recvuntil(b": ")
e_2 = int(r.recvline().rstrip().decode('utf-8').strip(" "))
#print(e_2)
#print("\n")
#print(flag)
r.recv()


r.sendline(b"2")
r.recv()
i_input = str((e_2*flag) % n).encode()
r.sendline(i_input)
r.recvuntil(b": ")
number = int(r.recvline().rstrip().decode('utf-8').strip(" "))
print(number)
r.recv()

#print(number/2)
