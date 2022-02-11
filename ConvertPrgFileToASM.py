import sys, getopt

# To run this program use this command 
# python3 ConvertPrgFileToASM.py --input=Filename --output=Filename

def convertToBinary(n):
    if n > 1:
        return convertToBinary(n//2)
    return "%s" % (n % 2)

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

file = open(inputfilename, "rb")

strNewFile = ""
intLineCounter = 0

theStartAddressLo = int.from_bytes(file.read(1) ,byteorder='big', signed=False)
theStartAddressHi = int.from_bytes(file.read(1) ,byteorder='big', signed=False)
theStartAddress = theStartAddressLo + (theStartAddressHi * 256)

strNewFile += "\n\nStartAddress: $%s \n" % hex(theStartAddress)[2:].upper().zfill(4)
strNewLine = ""

theByte = file.read(1)
while theByte:
    intTheByte = int.from_bytes(theByte,byteorder='big', signed=False)
    strHexByte = (hex(intTheByte)[2:]).upper()
    strHexByte = strHexByte.zfill(2)

    if strNewLine == "":
        strNewLine += "$" + strHexByte
    else:
        strNewLine += ", $" + strHexByte

    intLineCounter += 1
    if intLineCounter == 16:
        strNewFile += "//$" + hex(theStartAddress)[2:].upper().zfill(4) + "\n\t.byte " + strNewLine + "\n"
        intLineCounter = 0
        theStartAddress += 16
        strNewLine = ""

    theByte = file.read(1)

file.close()

file = open(outputfilename, "w")
file.write(strNewFile)
file.close()
