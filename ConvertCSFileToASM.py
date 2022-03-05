import sys, getopt

# To run this program use this command 
# python3 ConvertCSFileToASM.py --input=Filename --output=Filename

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
intCharCounter = 0

strNewFile += "\n\n\t// Character Number : %s " % intCharCounter
strNewFile += "($%s)" % hex(intCharCounter)[2:].zfill(2)
strNewFile += " HexOffset : $%s \n" % hex(intCharCounter * 8)[2:].zfill(4)

#theByte = file.read(1)
#theByte = file.read(1)
theByte = file.read(1)
while theByte:
    intTheByte = int.from_bytes(theByte,byteorder='big', signed=False)
    strBinaryByte = bin(intTheByte)[2:]
    strBinaryByte = strBinaryByte.zfill(8)

    strNewFile += "\t.byte %" + strBinaryByte + "\t\t\t// " + strBinaryByte.replace("0",".").replace("1","x") + "\n"

    intLineCounter += 1
    if intLineCounter == 8:
        intCharCounter += 1
        strNewFile += "\n\n\t// Character Number : %s " % intCharCounter
        strNewFile += "($%s)" % hex(intCharCounter)[2:].zfill(2)
        strNewFile += " HexOffset : $%s \n" % hex(intCharCounter * 8)[2:].zfill(4)

        intLineCounter = 0

    theByte = file.read(1)

file.close()

file = open(outputfilename, "w")
file.write(strNewFile)
file.close()
