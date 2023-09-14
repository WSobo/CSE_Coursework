from collections import Counter
from heapq import heappush, heappop
from PIL import Image
import numpy as np


class Codec:
    def __init__(self, delimiter='#'):
        self.delimiter = delimiter

    def encode(self, text):
        return ''.join([f'{ord(char):08b}' for char in text])

    def decode(self, data):
        return ''.join([chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8)]).strip(self.delimiter)


class CaesarCypher(Codec):
    def __init__(self, delimiter='#', shift=3):
        super().__init__(delimiter)
        self.shift = shift

    def encode(self, text):
        text = ''.join([chr((ord(char) + self.shift) % 256) for char in text])
        return super().encode(text)

    def decode(self, data):
        text = super().decode(data)
        return ''.join([chr((ord(char) - self.shift) % 256) for char in text])


class HuffmanCodes(Codec):
    def __init__(self):
        super().__init__()
        self.codes = {}

    def build_codes(self, char_freq):
        heap = [[weight, [char, ""]] for char, weight in char_freq.items()]
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        for pair in heap[0][1:]:
            char, code = pair
            self.codes[char] = code

    def encode(self, text):
        char_freq = Counter(text)
        self.build_codes(char_freq)
        return ''.join([self.codes[char] for char in text]) + self.delimiter

    def decode(self, data):
        inv_codes = {v: k for k, v in self.codes.items()}
        binary = ""
        text = ""
        for digit in data:
            binary += digit
            if binary in inv_codes:
                text += inv_codes[binary]
                binary = ""
        # Handling unexpected characters or improperly Huffman-encoded data
        if binary:
            text += binary
        return text.strip(self.delimiter)


if __name__ == '__main__':
    text = 'hello'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text)
    print('Binary:', binary)
    data = c.decode(binary)
    print('Text:', data)

    cc = CaesarCypher()
    binary = cc.encode(text)
    print('Binary:', binary)
    data = cc.decode(binary)
    print('Text:', data)

    h = HuffmanCodes()
    binary = h.encode(text)
    print('Binary:', binary)
    data = h.decode(binary)
    print('Text:', data)
