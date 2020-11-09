class AX25Frame:
##    def __init__(self, flag, addres, control, fcs):
##        self.flag = flag
##        self.addres = addres
##        self.control = control
##        self.fcs = fcs

    def __init__(self):
##        self.flag = '{:08b}'.format(0x82)
        self.flag = '{:08b}'.format(0x7e)
##        self.flag = '0' * 8 *	 200

    def decode(self):
        pass

    def is_flag(self, string):
        return string ==  self.flag


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
