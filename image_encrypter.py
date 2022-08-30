# Tim Jarvis
# Module 8: Linear Feedback Shift Registers
# Due Date: July 31, 2022

from PIL import Image
from lfsr import LFSR


class ImageEncrypter:

    # initial constructor call with required attributes seed, tap and file
    def __init__(self, seed, tap, file):
        self.seed = seed
        self.tap = tap
        self.file = file

    # encrypts the loaded file taking each pixel and applying lfsr to it
    def encrypt(self):
        image = Image.open(self.file)
        load_image = image.load()

        # LFSR method performed on seed to get new binary value for encryption
        LFSR1 = LFSR(self.seed, self.tap)
        new_LFSR = LFSR1.step()
        length = len(new_LFSR)

        # each pixel in image is iterated over and XOR'd with new LFSR value to get encrypted pixel
        for x in range(image.width):
            for y in range(image.height):

                # pixel from image is selected base on x, y position in the image
                pixel = load_image[x, y]
                encrypted_pixel = []

                # R, G, B values are iterated over for each pixel
                for i in range(3):
                    lfsr_decimal = 0

                    # lsfsr value is converted from binary to decimal
                    for n in range(-1, -(length + 1), -1):
                        lfsr_decimal += (int(new_LFSR[n]) * 2 ** (-n - 1))

                    # lfsr decimal and pixel decimal are XOR'd to create encrypted pixel color.
                    new_pixel = lfsr_decimal ^ pixel[i]
                    encrypted_pixel.append(new_pixel)

                    # new LFSR created for next pixel in image
                    LFSR1 = LFSR(new_LFSR, 5)
                    new_LFSR = LFSR1.step()

                # encrypted pixel x, y list values are converted to tuple to be put back in image in the proper format
                tup = tuple(encrypted_pixel)
                load_image[x, y] = tup

        image.save('encrypted.png')

        image.show('encrypted.png')


if __name__ == "__main__":
    Image1 = ImageEncrypter('10011010', 5, 'football.png')
    Image1.encrypt()

    Image2 = ImageEncrypter('10011010', 5, 'encrypted.png')
    Image2.encrypt()

