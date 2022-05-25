### base64 to RGB value
import string
alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
assert alphabet[0] == 'A'
assert alphabet[20] == 'U'
assert alphabet[62] == '+'

RGB_list = []
RGB_values = [0,85,170,255]
for i in range(4):
	for j in range(4):
		for k in range(4):
			RGB_list.append([RGB_values[i],RGB_values[j],RGB_values[k]])
RGB_list = tuple(RGB_list)

base642RGB_dict = {}

for i in range(64):
	base642RGB_dict[str(alphabet[i])] = RGB_list[i]

base64Index = {k: v for v, k in enumerate(alphabet)}
assert base64Index['A'] == 0
#input a list of base64 String
#return a 1D list of RBG pixel values
def base642RGB(base64_string):
	global base642RGB_dict
	global base64Index

	RGB_list = []
	
	for i in base64_string:
		RGB_list.append(base642RGB_dict[chr(i)])
	#print(l)
	return RGB_list
