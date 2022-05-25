import base64

def base64Encode(file_name):
	data = open(file_name, "rb").read()
	encoded = base64.b64encode(data)
	return encoded

def base64Decode(file_name, code):
	data = open(file_name, "w", encoding="utf8").read()
	decoded = base64.b64decode(encoded)
	outputFile.write(decoded)
	return 