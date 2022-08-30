# Tim Jarvis
# Module 8: Linear Feedback Shift Registers
# Due Date: July 31, 2022

# LFSR steps binary number shifting bits to the left and XOR last bit and tap bit to the first.
# LFSR: inputs seed and tap; tap = bit location of XOR value
# Outputs news binary value

class LFSR:

    # initial constructor call with required attributes seed and tap
    def __init__(self, seed, tap):
        self.seed = seed
        self.tap = tap

    # Get bit at tap location
    def bit(self):
        return self.seed[-self.tap]

    # determine new LFSR by shifting bits to the left and applying XOR
    def step(self):
        new_step = ''                                                  # initializing string
        i = -len(self.seed)
        new_bit = str(int(self.seed[i]) ^ int(self.bit()))

        for j in range(-(len(self.seed) - 1), 0):                      # shifting each bit to new string
            new_step += str(self.seed[j])

        new_lfsr = new_step + new_bit                                  # creating new LFSR

        # return new lfsr
        return new_lfsr

    # convert new lfsr into string instead of lfsr object
    def __str__(self):
        return self.step()


if __name__ == "__main__":
    LFSR1 = LFSR('0110100111', 2)
    LFSR2 = LFSR('0100110010', 8)
    LFSR3 = LFSR('1001011101', 5)
    LFSR4 = LFSR('0001001100', 1)
    LFSR5 = LFSR('1010011101', 7)

    string_LFSR1 = str(LFSR1)
    string_LFSR2 = str(LFSR2)
    string_LFSR3 = str(LFSR3)
    string_LFSR4 = str(LFSR4)
    string_LFSR5 = str(LFSR5)

    print(f'\n{string_LFSR1} {string_LFSR1[-1]}')
    print(f'{string_LFSR2} {string_LFSR2[-1]}')
    print(f'{string_LFSR3} {string_LFSR3[-1]}')
    print(f'{string_LFSR4} {string_LFSR4[-1]}')
    print(f'{string_LFSR5} {string_LFSR5[-1]}')
