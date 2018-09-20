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

# remaining_pixels = (w * h - len(msg_to_encode))/8
padding = "#"
bin_ver = bin(ord(padding))[2:].zfill(8)

# Generate noise
while len(msg_to_encode) < w*h:
    for bit in bin_ver:
        msg_to_encode.append(bit)

print("DONE!")

j = 2
for i in range(0, w*h):
    value_to_alter = im_data[j]
    bin_ver = list(bin(value_to_alter))
    bin_ver[-1] = msg_to_encode[i]
    im_data[j] = int(''.join(bin_ver[2:]).zfill(8), 2)
    j += 3


lol = bytes(im_data)
that = Image.frombytes('RGB', (w, h), lol)
that.save('encoded.png')
'''
# Get LSB of each pixel
for i in range(2, len(im_data), 3):
    value = im_data[i]
    print(i)

print(im.format, im.size, im.mode)
'''
