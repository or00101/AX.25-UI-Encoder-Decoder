from AX25Frame import AX25Frame as ax25


def get_odd_res(res):
    return (res, res + 1)[res % 2 == 0]

def meadian_window(samp_per_sym):
    res = round(samp_per_sym/2)
##    print(res)
    return get_odd_res(res)

def margin_bits(bit, half_window):
    return bit * half_window

def get_capture_with_margins(capture, half_window):
    start_marg = margin_bits(capture[0], half_window)
    end_marg = margin_bits(capture[len(capture) - 1], half_window)
    return start_marg + capture + end_marg

def bool_to_bit(boolean):
    return str(int(boolean))

def get_median(capture, i, half_window):
    lst = [int(capture[j]) for j in range(i - half_window, i + half_window + 1)]
##    print(lst)
    return bool_to_bit(sum(lst) > half_window)

def meadian_noise(capture, samp_per_sym):
    window = meadian_window(samp_per_sym)
    half_window = window//2
    capture = get_capture_with_margins(capture, half_window)
    res = ''
    
    for i in range(half_window, len(capture) - half_window):
        res += get_median(capture, i, half_window)
    
    return res

l1 = '110110001011111'
print(l1)
print(meadian_noise(l1, 5))
