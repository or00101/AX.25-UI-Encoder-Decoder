from AX25Frame import AX25Frame as ax25

def broadcast2ascii(broadcast):
    text = ''
    for i in range(len(broadcast) - 8):
        text += chr(int(broadcast[i: i + 4], 2))
    return text

def capture2bits(broadcast):
    res = ''
    for byte in broadcast:
        res += str(ord(byte))
    return res

def bits2hex(broadcast, spaces = ' '):
    hex_lst = []

    for i in range(0, len(broadcast) - 8, 8):
        byte = int(broadcast[i: i + 8], 2)
        hex_lst.append('{:02x}'.format(byte))
        
    return spaces.join(hex_lst)


def bits2spaced_hex(broadcast):
    res = ''
    for i in range(len(broadcast) - 4):
        text += h(int(broadcast[i: i + 4], 2))
    return text

def HexDigit2str(hex_digit):
    return str(hex_digit)[-1]

def make_realtime_bits(grc_output):
    res = ''

    for i in range(0, len(grc_output) - 2*22, 22):
        res += grc_output[i]

    return res

def good_frames(file_name = 'msgsinktest1.txt', count = 1024):

    f = open(file_name, 'r')
    ax = ax25()
    
    grc_output = f.read(count)
    print(capture2bits(grc_output)[-3400:-3038])
    print()
    print(capture2bits(grc_output)[:400])
    raw_capture = make_realtime_bits(grc_output[:-3038])
    raw_bits = capture2bits(raw_capture)
    #print(raw_bits)
    flags = ax.get_all_flags_indecies(raw_bits)

    frames_indecies = []

    for i in range(len(flags) - 1):
        frame_len = flags[i + 1] - flags[i]
        if frame_len % 4 == 0 and frame_len < 400:
            frames_indecies.append( (flags[i], flags[i + 1]) )
    print(flags)

##    b_start = 462360 #flags[1]
##    b_stop =  462608 #flags[2]
##    
##    b_start = ax.get_flag_index(raw_bits)
##    b_stop = ax.get_flag_index(raw_bits[b_start + 8:])
    
##    broadcast = raw_bits[b_start: b_stop + 8]
##    print(b_start, b_stop)
##    print(broadcast)
        
    f.close()

    return frames_indecies, raw_bits

def print_good_frames(file_name = 'msgsinktest1.txt', count = None):
    frames_indecies_lst, raw_bits = good_frames(file_name, count)

    for frame_start, frame_stop in frames_indecies_lst:
        
        print('\n\n')
        print("packet detected:\n")
        print(bits2hex(raw_bits[frame_start: frame_stop + 48]))




print_good_frames()
print('\n\n')
