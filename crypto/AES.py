from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Definizione dei parametri
key_hex = '94ce6518ec75b1e5a16f60e118fb1687591004355bf75b18820a21e2f5442ab7'
key = bytes.fromhex(key_hex)
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
plaintext = plaintext.encode('utf-8')

# Padding del plaintext
plaintext = pad(plaintext, AES.block_size, style='pkcs7')

# Definizione del vettore di inizializzazione
iv = get_random_bytes(AES.block_size)
print(iv.hex())

# Creazione dell'oggetto AES con la chiave e il vettore di inizializzazione
cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=24)

# Cifratura del plaintext
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# Conversione del ciphertext in esadecimale
ciphertext_hex = ciphertext.hex()

print("Testo cifrato (in esadecimale):", ciphertext_hex)
