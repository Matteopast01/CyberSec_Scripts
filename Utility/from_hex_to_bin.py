import binascii

# Hexadecimal representation of the gzip file
#hex_data=""


with open('hex_data', 'r') as file:
    # Read the entire contents of the file
    hex_data = file.read()
# Remove any spaces or newline characters
hex_data = hex_data.replace(" ", "").replace("\n", "")

# Convert hexadecimal string to binary
binary_data = binascii.unhexlify(hex_data)

# Write binary data to a file
with open("output", "wb") as f:
    f.write(binary_data)

print("Binary file 'output.gz' has been created.")
