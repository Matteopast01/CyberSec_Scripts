from pwn import *
import struct

r = remote("piecewise.challs.cyberchallenge.it", 9110)
flag = ""
while True:
	result = r.recvline()
	if b'empty' in result:
		r.sendline(b'')
 	
	elif b'integer' in result:
		splitted = result.split(b" ")
		numero = int(splitted[5].decode())
		lunghezza = splitted[8].decode()
		byte_order = splitted[9].decode()


	

	#little endian 23 bit -> "<I"
	#little endian 64 bit -> "<Q"
	#big endian 32 bit -> ">I"
	#big endian 64 bit -> ">Q"
		formato = ""
		prova = 0
		formato2 = ""
		if "32" in lunghezza:
			if "little" in byte_order:
				formato = "<I"
				prova = 32
				formato2 = "little"
			else:
				formato  = ">I"
				prova = 32
				formato2 = "big"

		if "64" in lunghezza:
			if "little" in byte_order:
				formato = "<Q"
				prova = 64

				formato2 = "little"
			else:
				formato  = ">Q"
				prova = 64
				formato2 = "big"
		print(numero)
		print(prova)
		my_bytes = numero.to_bytes(int(prova/8), byteorder= formato2)
		print(str(my_bytes))
		risposta = struct.pack(formato,numero)
		print(risposta)
		r.send(my_bytes)
	ans = r.recvline()

	print(ans)
	


	

r.close()
