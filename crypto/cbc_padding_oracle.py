from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from time import sleep

BLOCK_SIZE = 16

def is_padding_ok(byte_padding_to_check, r):
    hex_padding = byte_padding_to_check.hex()
    r.sendline(hex_padding.encode())
    response = r.recvline()
    padding_ok = False
    if b"Wow you are so strong at decrypting!" in response:
        padding_ok = True
    r.recv()
    return padding_ok

def attack(ciphertext, r):
    guessed_clear = b''

    split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
    blocks = split_string(ciphertext, BLOCK_SIZE)
    
    for block_n in range(len(blocks) - 1, 0, -1): #build pair of blocks starting from end of message
        spliced_ciphertext = blocks[block_n - 1] + blocks[block_n]

        decoded_bytes = b'?' * BLOCK_SIZE #output of block cipher decoding values

        ##GET VALUE OF SECRET BYTE byte
        for byte in range(BLOCK_SIZE - 1, -1, -1):
            new_pad_len = BLOCK_SIZE - byte

            #Build hacked ciphertext tail with values to obtain desired padding
            hacked_ciphertext_tail = b''
            for padder_index in range(1, new_pad_len):
                hacked_ciphertext_tail += bytearray.fromhex('{:02x}'.format(new_pad_len ^ decoded_bytes[byte + padder_index]))
            
            for i in range(0, 256):
                attack_str = bytearray.fromhex('{:02x}'.format((i ^ spliced_ciphertext[byte])))
                hacked_ciphertext = spliced_ciphertext[:byte] + attack_str + hacked_ciphertext_tail + spliced_ciphertext[byte + 1 + new_pad_len - 1:]

                if is_padding_ok(hacked_ciphertext, r):
   
                    test_correctness = hacked_ciphertext[:byte - 1] + bytearray.fromhex('{:02x}'.format((1 ^  hacked_ciphertext[byte]))) + hacked_ciphertext[byte:]
                    if not is_padding_ok(test_correctness, r):
                        continue
                    
                    decoded_bytes = decoded_bytes[:byte] + bytearray.fromhex('{:02x}'.format(hacked_ciphertext[byte] ^ new_pad_len)) + decoded_bytes[byte + 1:]
                    guessed_clear = bytearray.fromhex('{:02x}'.format(i ^ new_pad_len)) + guessed_clear
                    print(guessed_clear)
                    break
    
    return guessed_clear[:-guessed_clear[-1]] #remove padding!

if __name__ == '__main__':
    r = remote("padding.challs.cyberchallenge.it", 9033)
    r.recvuntil(b"flag\n")
    secret_flag = r.recvline().decode('utf-8').rstrip("\n")
    r.recv()
    print(attack(bytes.fromhex(secret_flag), r))
