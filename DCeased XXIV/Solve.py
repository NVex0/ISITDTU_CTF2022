from PIL import Image
import random

def xor(a):
	return a[0] ^ a[1]

def xor_tuple(a, b):
	return tuple(i for i in map(xor, zip(*[a, b])))

def rgba2int(rgba: tuple):
	ret = 0
	for i in range(3, -1, -1):
		ret += rgba[i] << 8*(3 - i)
	return ret

def int2rgba(n):
	r, g, b, a = tuple([(n >> 8*i) & 0xff for i in range(3, -1, -1)])
	return (r, g, b, a)

out = Image.open("/home/kali/Downloads/CTF/out.png")
pixout = out.load()
part = Image.open("/home/kali/Downloads/CTF/part.png")
pixpart = part.load()

strings = ""
count = 0

#get first 624 values of Rrgba.
for y in range(out.size[1]):
	for x in range(out.size[0]):
		ro, go, bo, ao = pixout[x, y]
		rp, gp, bp, ap = pixpart[x, y]
		temp = xor_tuple((ro, go, bo, ao), (rp, gp, bp, ap))
		strings += str(rgba2int(temp))
		count += 1
		if count == 624:
			break
		strings += "\n"
	if count == 624:
		break
strs = strings.split("\n")

#Using 624 rgba values above for predictor to fully recover Rrgba.
from mt19937predictor import MT19937Predictor
predictor = MT19937Predictor()
for i in strs:
	predictor.setrandbits(int(i), 32)
#Size of image is 720x720, meaning the image contains 518400 rgba values.
while(count < 518400):
	next_rand = predictor.getrandbits(32)
	strings += "\n"
	strings += str(next_rand)
	count += 1
strings = strings.split("\n")

#Recover the flag.
flag = Image.new(out.mode, out.size)
flagpix = flag.load()
i = 0
for y in range(out.size[1]):
	for x in range(out.size[0]):
		ro, go, bo, ao = pixout[x, y]
		rn, gn, bn, an = int2rgba(int(strings[i]))
		flagpix[x, y] = xor_tuple((ro, go, bo, ao), (rn, gn, bn, an))
		i += 1
flag.show()
	
