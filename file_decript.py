from AX25Frame import AX25Frame as ax25
from g3ruh_scrambler import g3ruh_descrambler
from noise_module import meadian_noise

def broadcast2ascii(broadcast):
    text = ''
    for i in range(len(broadcast) - 8):
        text += chr(int(broadcast[i: i + 4], 2))
    return text

def capture2bits(capture):
    res = ''
    for byte in capture:
        res += str(ord(byte))
    return res

def bits2hex(bitstream, sep = ' '):
    hex_lst = []

    for i in range(0, len(bitstream) - 8, 8):
        byte = int(bitstream[i: i + 8], 2)
        hex_lst.append('{:02x}'.format(byte))
        
    return sep.join(hex_lst)

def HexDigit2str(hex_digit):
    return str(hex_digit)[-1]

def capture_to_symbols(capture, samples_per_symbol):
    res = '0'*8
    streak = '1'
    streak_counter = 0

    for bit in capture:
        if bit == streak:
            streak_counter += 1
        else:
            res += streak * round(streak_counter/samples_per_symbol)
            streak = bit
            streak_counter = 1

    
    return res + '0' * 8

def good_frames(file_name, count, samples_per_symbol):

    f = open(file_name, 'r')
    ax = ax25()
    
    capture = f.read(count)

    bits = meadian_noise(capture, samples_per_symbol)
    broadcast = capture_to_symbols(capture, samples_per_symbol)
    broadcast = g3ruh_descrambler(broadcast)
        
    flags = ax.get_all_flags_indecies(broadcast)

    frames_indecies = []

    for i in range(len(flags) - 1):
        frames_indecies.append( (flags[i], flags[i + 1]) )

    f.close()

    return frames_indecies, broadcast

def print_good_frames(file_name, count, samples_per_symbol):
    frames_indecies_lst, broadcast = good_frames(file_name, count, samples_per_symbol)

    for frame_start, frame_stop in frames_indecies_lst:
        print('\n')
        print("packet detected:")
        print(bits2hex(broadcast[frame_start: frame_stop]))
    print("\n" + str(len(frames_indecies_lst)) + " Packets found.\n")

    l = '00 00'.split()
    check = ''.join(['{:08b}'.format(int(n, 16)) for n in l])
    print(' '.join(l), 'was' + (' not', '')[check in broadcast], 'found in the broadcast.\n')

print_good_frames('bb_20-122-222_binary_bin', None,10)
