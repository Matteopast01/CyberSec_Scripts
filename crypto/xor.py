import base64

#key and text must be byte type!
def xor_bytes(key, text, is_key_repeated=False):
    # Repeat the key until its length matches or exceeds the ciphertext length
    if is_key_repeated:
        key = (key * (len(text) // len(key) + 1))[:len(text)]

    # Perform XOR operation
    result = bytes(x ^ y for x, y in zip(key, text))
    return result


#key and text must of string type!
def stringXOR(key, text):
    return "".join(chr((ord(text[x]) ^ ord(key[x % len(key)]))) for x in range(len(text)))







if __name__ == "__main__":

    cipher1 = base64.b64decode("cSA0FDk7RRhVNkY3TEdZKycUKCdDGF4hUSBMXFEgfhQZPRdZRXdDOxhZWSBwWThyQ1cRJF0/HF1VbjFHOSdFXR93eSBMVVk9IFs5O1lfETRbPBhYXjs1UGo7QxheMVI3AlVZIDcUKyBFWV8wXTwLEVkgcEMvfBd9SSNGNwFYRDdwVTlyXl4RNUY3DVpWLyNAajNQSlQyWTcCRR5uH1IscllXRndZOx9FQisjR2oiRVdHPlA3CBFfOyQUIj1FSlg1WDdMXkAnPl0lPEQWEQdGNxpQWSI1UGo/RRhFOFg3HlBSIikULjtEW14iRiEJEVE9I0E4M1lbVHdRIRhYXS8yWC9yVkhBO1UnCFRUbiRbaiFYFhEfXT9MVEYrIk0+Ol5WVndZNwBQXi04WyYrF01fNFs/AV5eIikUKCdDGEI4WDsPWEQ7NFFqO1lQUDVdJgVfV24gRiU4UltFPls8TF5WKH4UCT1ZVlQ0QDsDXxA9JF0nJ1tZRTJQcglCRCc9VT47WV8RMkwxCV1cKz5XL3JWVhEjW3IFXEA8NUc5O1hWHw==")


    key = bytes.fromhex("304e50344a523738315734526c31")

    #parameters are byte objects
    result = xor_bytes(key, cipher1, True)

    #parameters are string objects
    key = bytes.fromhex("304e50344a523738315734526c31").decode('utf-8')
    cipher1 = cipher1.decode('utf-8')
    result = stringXOR(key, cipher1)   

