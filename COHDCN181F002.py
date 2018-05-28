import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type = str, required = True)
args = parser.parse_args()

line = 0
length = 0

no = 0
read = 2

file = open(args.file, "rb")

rawContent = file.read()

strContent = str(rawContent)
strContent = strContent.replace(" ", ".")
strContent = strContent[:len(strContent)-1]

length = int(len(strContent))
if length < 16:
    line = 1
else:
    line = length/16 +2-1

for c in range(int(line)):
    text = "{:#08x}".format(no) + " ???? "
    text += " ".join("{:02x}".format(ord(x)) \
        for x in strContent[read:read+16])
    text += " ???? " + strContent[read:read+16]
    no += 16
    read += 16

    print(text)

else:
    print("No file open")
