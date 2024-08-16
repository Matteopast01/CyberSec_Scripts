def circular_left_shift(num, shift):
    # Ensure the shift value is reduced modulo 8
    shift %= 8
    
    # Perform the circular left shift
    return ((num << shift) | (num >> (8 - shift))) & 0xFF

    



if __name__ == '__main__':
	with open('flag.txt.aes', 'rb') as file:
		bytes_read = file.read()

	counter = 1;
	result=[]
	for byte in bytes_read:
		result.append(circular_left_shift(byte,counter))
		counter = counter +1

	print(bytes(result))
		
	






