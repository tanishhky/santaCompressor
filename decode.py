import heapq

def huffman_decode(encoded_data, codes):
    decoded_data = ""
    current_code = ""
    
    while encoded_data:
        found = False
        for code, symbol in codes.items():
            if encoded_data.startswith(code):
                decoded_data += symbol
                encoded_data = encoded_data[len(code):]
                found = True
                break

        if not found:
            current_code += encoded_data[0]
            encoded_data = encoded_data[1:]

        # Add a print statement to check the decoded data at each step
        print(f"Decoded Data: {decoded_data}")

    return decoded_data

if __name__ == "__main__":
    input_file = "encoded.huf"
    output_file = "output.txt"

    codes = {}
    encoded_data = ""

    with open(input_file, 'rb') as f:
        reading_codes = True
        for line in f:
            line = line.decode('utf-8').strip()
            if line == "EOF":
                reading_codes = False
            elif reading_codes:
                code = line
                symbol = chr(0)  # Placeholder for symbol, since it's not provided in the file
                codes[code] = symbol
            else:
                encoded_data += line
        
        # Add a print statement to check the encoded data
        print(f"Encoded Data: {encoded_data}")

    decoded_data = huffman_decode(encoded_data, codes)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_data)
