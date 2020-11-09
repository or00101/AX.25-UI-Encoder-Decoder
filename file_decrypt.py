from AX25Frame import AX25Frame as ax25
from g3ruh_scrambler import g3ruh_descrambler
from g3ruh_scrambler import g3ruh_scrambler
from bb_recording_to_sym import make_sym_file
from print_packets import print_packets
from print_packets import bits_to_hex


def get_packet(bits, start, stop):
    return bits[start: stop]

def get_packets_list(sym_file_name):
    
    f = open(sym_file_name, 'r')
    
    bits = f.read()
    bits = g3ruh_scrambler(bits)

    ax = ax25()

    flags_lst = ax.get_all_flags_indecies(bits)

    pack_lst = []

    for i in range(len(flags_lst)):
        try:
            packet = get_packet(bits, flags_lst[i], flags_lst[i] + 2048)
            pack_lst.append(packet)
        except:
            print('oof...')

    f.close()

    return pack_lst


def save_packets(cap_file_name, pack_lst, save_binary = False):
    pack_file_name = cap_file_name + '_packets'

    if save_binary:
        pack_file_name += '_binary'
    else:
        pack_file_name += '_hex'
    
    pack_file = open(pack_file_name, 'w')

    contents = ''
    if save_binary:
        contents = '\n'.join(pack_lst)
    else:
        contents = '\n'.join([bits_to_hex(packet) for packet in pack_lst])

    pack_file.write(contents)
    
    pack_file.close()


def main(cap_file_name, samples_per_symbol):

    sym_file_name = make_sym_file(cap_file_name, samples_per_symbol)

    # list containing all the (descrambled) packets.
    pack_lst = get_packets_list(sym_file_name)

    print_packets(pack_lst)
    save_packets(cap_file_name, pack_lst)


main('bb_20-122-222_sliced_samp', 40)
