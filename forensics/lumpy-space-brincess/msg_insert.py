from PIL import Image
import random
random.seed(25)

im = Image.open('ohmyglob.jpg')
w, h = im.size[0], im.size[1]
flag = "HNF{0h_My_gL0b_I_aM_th3_M0St_s1gN1f1cANt_pr1nCE55!!}"
im_data = list(im.tobytes())

# Bits of flag
flag_bits_to_encode = []
# Completed data to encode into full image
msg_bits_to_encode = []
for c in flag:
    bin_ver = bin(ord(c))[2:].zfill(8)
    for bit in bin_ver:
        flag_bits_to_encode.append(bit)

padding = "#"
padding_bin = bin(ord(padding))[2:].zfill(8)

# Generate noise & fill up msg_bits_to_encode
i = 0
while len(msg_bits_to_encode) < w*h:
    option = random.randint(0, 1000)
    if i >= len(flag_bits_to_encode):
        for bit in padding_bin:
            msg_bits_to_encode.append(bit)
    else:
        if option < 999:
            for bit in padding_bin:
                msg_bits_to_encode.append(bit)
        else:
            for j in range(i, i+8):
                msg_bits_to_encode.append(flag_bits_to_encode[j])
            i += 8


# Encode msg into LSBs of original image
j = 2
for i in range(0, w*h):
    value_to_alter = im_data[j]
    bin_ver = list(bin(value_to_alter))
    bin_ver[-1] = msg_bits_to_encode[i]
    im_data[j] = int(''.join(bin_ver[2:]).zfill(8), 2)
    j += 3


new_img = Image.frombytes('RGB', (w, h), bytes(im_data))
new_img.save('encoded.png')
