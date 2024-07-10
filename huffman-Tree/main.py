import heapq
from collections import defaultdict

def huffman(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))



def decode_Huffman(encoded_data, huffman_tree):
    decode_map = {code: char for char, code in huffman_tree}
    decoded_data = ""
    code = ""

    for bit in encoded_data:
        code += bit
        if code in decode_map:
            decoded_data += decode_map[code]
            code = ""  # Reset the code for the next character

    return decoded_data

# encoding huffman
def encode_Huffman(data, huffman_tree):
    code_map = {char: code for char, code in huffman_tree}
    encoded_data = ''.join(code_map[char] for char in data)
    return encoded_data

def main():
    while True:
        data = input("Enter a string to encode (if '0' stops): ")
        if data == '0':
            break

        huffman_tree = huffman(data)
        encoded_data = encode_Huffman(data, huffman_tree)
        print("encoded data is:", encoded_data)

        decoded_data = decode_Huffman(encoded_data, huffman_tree)
        print("decoded data is:", decoded_data)

if __name__ == "__main__":
    main()
