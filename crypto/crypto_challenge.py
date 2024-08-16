import itertools
import string
import base64


# Generate all possible combinations of 4 characters using lowercase ASCII letters
all_combinations = itertools.product(string.ascii_lowercase, repeat=4)

# Convert the combinations into strings
all_strings = [''.join(combination) for combination in all_combinations]

def encrypt(clear, key):
  enc = []
  for i in range(len(clear)):
    key_c = key[i % len(key)]
    enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
    enc.append(enc_c)
  return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')


def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)

def find_collisions(dict1, dict2):
    collisions = set()
    
    # Iterate over the values of the first dictionary
    for value in dict1.values():
        # If the value is present in both dictionaries, it's a collision
        if value in dict2.values():
            collisions.add(value)
    
    return collisions




if __name__ == '__main__':
    all_combinations = itertools.product(string.ascii_lowercase, repeat=4)

    # Convert the combinations into strings
    all_strings = [''.join(combination) for combination in all_combinations]
    all_possible_encryptions = {}
    for key1 in all_strings:
        all_possible_encryptions[key1] = encrypt("See you later in the city center", key1)

    all_possible_decryptions = {}
    for key2 in all_strings:
        print(key2)
        decryption = decrypt("QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE=", key2)
        if decryption in all_possible_encryptions.values():
            for key1, value1 in all_possible_encryptions.items():
                if value1 == decryption:
                    print("Collision Found!")
                    print("Key1:", key1)
                    print("Key2:", key2)
                    print("COLLISIONEEEEEEEEEE:")
                    break  # Exit inner loop once collision is found




        


