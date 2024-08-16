from Crypto.Hash import SHA3_384

from Crypto.Hash import HMAC, SHA224
from Crypto.Util.Padding import pad
from Crypto.Hash import SHA224
from Crypto.Hash import SHA384
import hashlib
from Crypto.PublicKey.DSA import import_key

def function1 ():
	msg = 'hash_me_pls'
	hash_object = SHA3_384.new(data=msg.encode())
	hex_digest = hash_object.hexdigest()

	print(hex_digest)

def function2(): 
	key_hex = '4225e8abb1202ec0af0e3c0346c62aff3fd93d46392ddb0f5c08706e2f1ff4fb'
	msg = 'La mia integrità è importante!'

	# Convert the hexadecimal key to bytes
	key = bytes.fromhex(key_hex)

	# Pad the message if necessary
	#msg = pad(msg.encode(), block_size=64)

	# Initialize HMAC with SHA-224 and the provided key
	hmac_object = HMAC.new(key, digestmod=SHA224)

	# Update HMAC object with the message
	hmac_object.update(msg.encode())

	# Get the hexadecimal digest of the HMAC
	hex_digest = hmac_object.hexdigest()

	print(hex_digest)

def function3():
	key_hex = '3082025c0201003082023506072a8648ce3804013082022802820101009d98c570cdb11eb47de6ce81270ce5ab29d305620343ddbc57b379449486788c743d28400f73d3f6a287f3e4aae07057336130c7f2fdac1bcd0b1e6f5cab3729edd8771edc7f1730958ff2f21b53d7f03e7215452b0c99d16dca65c39334c5e9542da9ca5d3b8ebe84d15724ddc52d2391e9e635688f14c6f2801e3fe9964555921919bda4f5501fd47c0e1c282bfc84caeb91007e7e83baf4f3b591805d3742a204bb248c24d31019e5cf9c5939aee5b4f5880eab79c24747d68361361cea3a766868679a326c30c2026b06ba72b67097fa88627e2c5543671bc5ae009592fb30ccf15b82aa917cb6571d7c239290926d8d929943f65d517e10d67c9cb4c575021d00e373d1ea94ece38a27d8bca83ea5010d6d64e4610f1f9016a9c7a8b9028201004016fed5706a533f22a61f848868a76155a05e93c31768dfe7df0d33561354a36af4351efa1e060785aa953da58eaefc359f273c82ba28231dad7d612b26494fd9926480101b6ee078c1b199e2dc01b56f80ee2acb049d731eee30aebdc32770ab242a68362a98ea8c442327b79c381dbb7e71e85d401ee85e2a458559e423736c52151da255804aebb3f1ea7b14a66a8f02a0dcc52bba81750e7b2660dc4acdf83f9c0e2399164020315642fa3e4fcbc8f8d39d3caeafb44121a84df2054b4283f0b4cedccb1d72713ea4fceb3702b0e7d7b204eb2ce99cb5f522f3658c2a43ddf5d78c23f6f4e649adf6fe7a98306ea30054cc3a2c58701c40c910873affaf041e021c127185607eaa94c81972d98d419a58a1eb610d8b7d07f61bc5fe5e54'
	byte_key = bytes.fromhex(key_hex)
	dsa = import_key(byte_key)
	print(dsa.q)

if __name__ =="__main__":
	function3()
