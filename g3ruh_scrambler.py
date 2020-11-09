def _get_margin(margin):
    return '1' * margin

def _real_bit(bit):
    return int(bit) - int('0')

def _exor(lst):
    bit_lst = [int(char) - int('0') for char in lst]
    res = 0
    for bit in bit_lst:
        res = res ^ bit
    return str(res)

def _scramble(prev_bits, bit):
    if len(prev_bits) < 17:
        return _exor([bit, '0', '0'])
    x17 = prev_bits[-17]
    x12 = prev_bits[-12]
    return _exor([bit, x12, x17, '0'])

def g3ruh_descrambler(bits):
    margin = 17
    res = _get_margin(margin)

    for bit in bits:
        res += _scramble(res, bit)

    return res[margin:]

def g3ruh_scrambler(bits):
    margin = 17
    bits = _get_margin(margin) + bits
    res = ''

    for i in range(margin, len(bits)):
        res += _scramble(bits[:i], bits[i])

    return res


########################################################################
##############################  TESTS  #################################
########################################################################
import random

def _make_random_message(length):
    res = ''
    for i in range(length):
    	res += str(random.randint(0, 1))
    return res

def _show(msg):
    scrm = g3ruh_scrambler(msg)
    descrm = g3ruh_descrambler(scrm)
    print('\nOriginal:\n' + msg)
    print('Scrambled:\n' + scrm)
##    print(g3ruh_descrambler(msg))
    print('Descrambled:\n' + descrm)
##    print(g3ruh_scrambler(g3ruh_descrambler(msg)))
    print('\nIs descrambled = original? - ' + ('No.', 'Yes.')[descrm == msg])

##_show(_make_random_message(78))

##l1 = '10110101011111010111101011110000111110101110001101011'
##print(l1, "\n")
##s = g3ruh_scrambler(l1)
##print(s, "\n")
##d = g3ruh_descrambler(s)
##print(d)
