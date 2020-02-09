import cv2
import unicodedata as ud
from sys import argv

# python img.py airtel.png 80 120 1
# 1 image
# 2 scale percentage
# 3 threshold
# 4 invert image

check = 255 if argv[4] == '0' else 0
x_gap = 1
y_gap = 1

img = cv2.imread(argv[1], cv2.IMREAD_GRAYSCALE)
scale_percent = int(argv[2])
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = int(argv[3])
img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

# cv2.imshow('image',img)
# cv2.waitKey(0)

y_max, x_max = img.shape
# print img.shape

img_str = ''

i=0; j=0

while i < y_max:

	if i+3 >= y_max:
		break
	j=0
	while j < x_max:

		if j+2 >= x_max:
			break
		name = ''
		if img[i][j] == check:
			name+='1'
		if img[i+1][j] == check:
			name+='2'
		if img[i+2][j] == check:
			name+='3'
		if img[i][j+1] == check:
			name+='4'
		if img[i+1][j+1] == check:
			name+='5'
		if img[i+2][j+1] == check:
			name+='6'
		if img[i+3][j] == check:
			name+='7'
		if img[i+3][j+1] == check:
			name+='8'

		if name == '':
			lookup = 'BRAILLE PATTERN BLANK'
		else:
			lookup = 'BRAILLE PATTERN DOTS-'+name

		# print lookup
		img_str += ud.lookup(lookup)

		j+=2
		j+=x_gap
	img_str+='\n'
	i+=4
	i+=y_gap

# print img_str
f = open('output.txt','w')
f.write(img_str.encode('utf8'))
f.close()
print(img_str)