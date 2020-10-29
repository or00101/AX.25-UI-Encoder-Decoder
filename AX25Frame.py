class AX25Frame:
##    def __init__(self, flag, addres, control, fcs):
##        self.flag = flag
##        self.addres = addres
##        self.control = control
##        self.fcs = fcs
    def __init__(self):
        pass

    def decode(self):
        pass

    def is_flag(self, string):
        return string == '01111110'

    def get_flag_index(self, broadcast):
        for i in range(0, len(broadcast) - 8):
            #print(broadcast[i: i + 8])
            if self.is_flag(broadcast[i: i + 8]):
                return i
        return -1

    def get_all_flags_indecies(self, broadcast):
        i_lst = []

        for i in range(0, len(broadcast) - 8):
            #print(broadcast[i: i + 8])
            if self.is_flag(broadcast[i: i + 8]):
                i_lst.append(i)
        return i_lst
