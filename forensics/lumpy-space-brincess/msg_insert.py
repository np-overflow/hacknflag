from PIL import Image
import random
random.seed(25)

im = Image.open('ohmyglob.jpg')
w, h = im.size[0], im.size[1]
msg = "HNF{n0t_l3aSt_s1gnif1c4nt}"
im_data = list(im.tobytes())

# Complete data to encode into full image
msg_to_encode = []
for c in msg:
    bin_ver = bin(ord(c))[2:].zfill(8)
    for bit in bin_ver:
        msg_to_encode.append(bit)

padding = "#"
padding_bin = bin(ord(padding))[2:].zfill(8)

# Generate noise
while len(msg_to_encode) < w*h:
    for bit in padding_bin:
        msg_to_encode.append(bit)


# Encode msg into LSBs of original image
j = 2
for i in range(0, w*h):
    value_to_alter = im_data[j]
    bin_ver = list(bin(value_to_alter))
    bin_ver[-1] = msg_to_encode[i]
    im_data[j] = int(''.join(bin_ver[2:]).zfill(8), 2)
    j += 3


new_img = Image.frombytes('RGB', (w, h), bytes(im_data))
new_img.save('encoded.png')
