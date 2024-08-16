from Crypto.Cipher import ChaCha20

# Definizione dei parametri
key_hex = 'e26f976471a15b3f9f18fc4df91427459b18c7ca0d4b6296b9d49ec584e2bf5f'
key = bytes.fromhex(key_hex)
ciphertext_hex = '92f6aeacb980f23e1dfa74d3f3d27713599ce1f817b1949bf115ac0b'
ciphertext = bytes.fromhex(ciphertext_hex)
nonce_hex = '53b007d8209fd548'
nonce = bytes.fromhex(nonce_hex)

# Creazione dell'oggetto ChaCha20 con la chiave e il nonce
cipher = ChaCha20.new(key=key, nonce=nonce)

# Decifratura del ciphertext
plaintext = cipher.decrypt(ciphertext)

# Decodifica del plaintext da byte a stringa ASCII
plaintext_ascii = plaintext.decode('utf-8')

print("Testo in chiaro (ASCII):", plaintext_ascii)
