def _broadcast2ascii(broadcast):
    text = ''
    for i in range(len(broadcast) - 8):
        text += chr(int(broadcast[i: i + 4], 2))
    return text


def bits_to_hex(bits, sep = ' '):
    hex_lst = []

    for i in range(0, len(bits) - 8, 8):
        byte = int(bits[i: i + 8], 2)
        hex_lst.append('{:02x}'.format(byte))
        
    return sep.join(hex_lst)

def _informed_pack(packet, data):
    info = 'Packet # ' + str(data)
    return info + '\n' + packet

def print_packets(pack_lst):

    pack_lst = [bits_to_hex(packet) for packet in pack_lst]
    pack_lst = [_informed_pack(pack_lst[i], i) for i in range(len(pack_lst))]

    print('\n\n'.join(pack_lst))
