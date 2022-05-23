import base64
data = open("SF trip cost.xlsx", "r").read()
encoded = base64.b64encode(data)

decoded = base64.b64decode(encoded)

outputFile = open("SFTripCopy.xlsx", "w")
outputFile.write(decoded)