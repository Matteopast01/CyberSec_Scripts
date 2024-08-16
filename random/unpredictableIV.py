from pwn import *
import json
from Crypto.Util.Padding import pad

r = remote("predictable.challs.cyberchallenge.it", 9034)
print(r.recv())
r.sendline(b"1")
print(r.recv())
r.sendline(b"matteo")
login_token = r.recv().split(b" ")[3][:-3]
r.sendline(b"4")
iv = r.recv().split(b"\n1")[0].decode()
print(iv)
print(iv.replace("'", '"'))
iv_dict = json.loads(iv.replace("'", '"'))
my_iv = bytes.fromhex(iv_dict["matteo"])
admin_iv = bytes.fromhex(iv_dict["admin"])
r.sendline(b"2")
r.recv()
r.sendline(login_token)
command = pad(b"get_flag", 16)
command_plain_text = bytes([a^b for (a,b) in zip (command, my_iv)])
command_plain_text = bytes([a^b for (a,b) in zip (command_plain_text, admin_iv)])
command_plain_text = command_plain_text.hex()
r.sendline(command_plain_text.encode())
print(r.recv())
command_token = r.recv().split(b"\n1")[0].split(b":")[1].strip().decode()
print(len(command_token))
command_token = iv_dict["admin"] + command_token[32:64] 

r.sendline(b"3")
print(r.recv())
r.sendline(command_token)
print(r.recv())

