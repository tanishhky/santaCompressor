import heapq
from collections import defaultdict

class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1

    heap = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node, code='', base=0):
    if node is None:
        return {}
    
    if node.symbol is not None:
        return {node.symbol: (code, base)}
    
    left_codes = generate_huffman_codes(node.left, code + '0', base)
    right_codes = generate_huffman_codes(node.right, code + '1', base + 1)
    
    left_codes.update(right_codes)
    return left_codes

def uniform_length_codes(codes):
    max_length = max(len(code) for code in codes.values())
    uniform_codes = {}
    for symbol, (code, base) in codes.items():
        uniform_code = code + '0' * (max_length - len(code))
        uniform_codes[symbol] = (uniform_code, base)
    return uniform_codes

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = generate_huffman_codes(root)
    uniform_codes = uniform_length_codes(codes)
    encoded_data = ""
    base = 0

    for symbol in data:
        code, base = uniform_codes[symbol]
        encoded_data += code

    return encoded_data, uniform_codes

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "encoded.huf"

    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()
    
    encoded_data, codes = huffman_encode(data)

    with open(output_file, 'wb') as f:
        for symbol, (code, base) in codes.items():
            f.write(f"{symbol}\t{code}\t{base}\n".encode('utf-8'))
        f.write(b"EOF\n")
        f.write(encoded_data.encode('utf-8'))
