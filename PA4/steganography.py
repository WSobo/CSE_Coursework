from codec import Codec, CaesarCypher, HuffmanCodes
from PIL import Image
import matplotlib.pyplot as plt


class Steganography:
    def __init__(self):
        self.text = ''
        self.binary = ''

    def print(self):
        print(f'Text: {self.text}')
        print(f'Binary: {self.binary}')

    def show(self, filein):
        try:
            img = Image.open(filein)
            plt.imshow(img)
            plt.show()
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def encode(self, filein, fileout, message, codec):
        try:
            codecs = {'binary': Codec(), 'caesar': CaesarCypher(),
                      'huffman': HuffmanCodes()}
            self.text = message
            self.binary = codecs[codec].encode(
                message + codecs[codec].delimiter)

            img = Image.open(filein)
            binary_message = iter(self.binary)
            pixels = img.load()

            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    pixel = list(pixels[i, j])
                    for k in range(3):
                        pixel[k] = int(f'{pixel[k]:08b}'[:-1] +
                                       next(binary_message, '0'), 2)
                    pixels[i, j] = tuple(pixel)

            img.save(fileout)
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decode(self, filein, codec):
        try:
            codecs = {'binary': Codec(), 'caesar': CaesarCypher(),
                      'huffman': HuffmanCodes()}
            img = Image.open(filein)
            pixels = img.load()
            binary_message = ''

            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    for k in range(3):
                        binary_message += f'{pixels[i, j][k]:08b}'[-1]

            self.binary = binary_message.rstrip('0')
            self.text = codecs[codec].decode(self.binary)
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':

    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    print('Everything works!!!')
