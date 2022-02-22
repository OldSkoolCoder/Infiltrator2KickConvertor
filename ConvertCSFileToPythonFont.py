import sys, getopt

# To run this program use this command 
# python3 ConvertCSFileToPythonFont.py --input=Filename --output=Filename

full_cmd_arguments = sys.argv

# Keep all but the first
argument_list = full_cmd_arguments[1:]

#print (argument_list)

short_options = "hi:o:"
long_options = ["help", "input=", "output="]

inputfilename = ""
outputfilename = ""

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-o", "--output"):
        print ("Enabling Output mode (%s)" % (current_value))
        outputfilename = current_value
    elif current_argument in ("-h", "--help"):
        print ("Displaying help")
    elif current_argument in ("-i", "--input"):
        print (("Enabling input mode (%s)") % (current_value))
        inputfilename = current_value

binFont = []
file = open(inputfilename, "rb")
theByte = file.read(1)
while theByte:
    binChar = []
    for bytes in range(8):
        intTheByte = int.from_bytes(theByte,byteorder='big', signed=False)
        binChar.append(intTheByte)
        theByte = file.read(1)
    binFont.append(binChar)
file.close()

newFont = []
for char in binFont:
    newchar = []
    for bit in range(7,-1,-1):
        newbyte = 0
        for x in range(8):
            #print (char[x] , pow(2,bit),(char[x] & pow(2,bit)))
            if (char[x] & pow(2,bit)) == pow(2,bit):
                newbyte = newbyte | pow(2,x)
        newchar.append(newbyte)
    newFont.append(newchar)


intCharCounter = 0
strFile = outputfilename.replace(".py","") + " = [\n\n"
for char in newFont:
    strLine = "\t[ # Character Number : %s " % intCharCounter
    strLine += "\n"
    for byte in char:
        strBinaryByte = bin(byte)[2:]
        strBinaryByte = strBinaryByte.zfill(8)
        strLine += "\t\t0b" + strBinaryByte + ",\t# " + strBinaryByte.replace("0",".").replace("1","x") + "\n"
    strLine += "\t],\n"
    intCharCounter += 1
    strFile += strLine

strFile += "]"

file = open(outputfilename, "w")
file.write(strFile)
file.close()
