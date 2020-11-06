class AX25Frame:
##    def __init__(self, flag, addres, control, fcs):
##        self.flag = flag
##        self.addres = addres
##        self.control = control
##        self.fcs = fcs
    def __init__(self):
##        self.flag = '{:08b}'.format(0x82)
        self.flag = '{:08b}'.format(0x7e)
##        self.flag = '100110001001100001000000'
##        self.flag = '1001100010011000100000010000001000000111000001101000111100001101000110100001110011011011000110000111111100001001001110111011100111100101111001011101001000001110100'

    def decode(self):
        pass

    def is_flag(self, string):
##        return string == '01111110'
        return string ==  self.flag
##        return string == '100110000100000001000000010000001110000001101000'

    def get_flag_index(self, broadcast):
        return broadcast.index(self.flag)

    def get_all_flags_indecies(self, broadcast):
        flag_indecies = []
        i = 0;
        while (self.flag in broadcast[i:]):
            i = broadcast.index(self.flag, i)
            flag_indecies.append(i)
            i += 1
        print(flag_indecies)
        return flag_indecies
