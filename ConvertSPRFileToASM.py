import sys, getopt

# To run this program use this command 
# python3 ConvertSPRFileToASM.py --input=Filename --output=Filename

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
intSpriteCounter = 0

strNewFile += "\n\n\t// Sprite Number : %s " % intSpriteCounter
strNewFile += "($%s)" % hex(intSpriteCounter)[2:].zfill(2)
strNewFile += " HexOffset : $%s \n" % hex(intSpriteCounter * 64)[2:].zfill(4)

theByte1 = file.read(1)
while theByte1:
    theByte2 = file.read(1)
    theByte3 = file.read(1)

    intTheByte1 = int.from_bytes(theByte1,byteorder='big', signed=False)
    strBinaryByte1 = bin(intTheByte1)[2:]
    strBinaryByte1 = strBinaryByte1.zfill(8)

    intTheByte2 = int.from_bytes(theByte2,byteorder='big', signed=False)
    strBinaryByte2 = bin(intTheByte2)[2:]
    strBinaryByte2 = strBinaryByte2.zfill(8)

    intTheByte3 = int.from_bytes(theByte3,byteorder='big', signed=False)
    strBinaryByte3 = bin(intTheByte3)[2:]
    strBinaryByte3 = strBinaryByte3.zfill(8)

    strNewFile += "\t.byte %" + strBinaryByte1 + ", %" + strBinaryByte2 + ", %" + strBinaryByte3 + "\t\t// "
    strNewFile += strBinaryByte1.replace("0",".").replace("1","x") + " " + strBinaryByte2.replace("0",".").replace("1","x") + " " + strBinaryByte3.replace("0",".").replace("1","x") + "\n"

    intLineCounter += 1
    if intLineCounter == 21:
        TheByteLeft = file.read(1)
        intTheByteLeft = int.from_bytes(TheByteLeft,byteorder='big', signed=False)
        strBinaryLeft = bin(intTheByteLeft)[2:]
        strBinaryLeft = strBinaryLeft.zfill(8)
        strNewFile += "\t.byte %"+ strBinaryLeft + "\t\t\t\t\t\t\t\t// " + strBinaryLeft.replace("0",".").replace("1","x") + "\n"

        intSpriteCounter += 1
        strNewFile += "\n\n\t// Sprite Number : %s " % intSpriteCounter
        strNewFile += "($%s)" % hex(intSpriteCounter)[2:].zfill(2)
        strNewFile += " HexOffset : $%s \n" % hex(intSpriteCounter * 64)[2:].zfill(4)

        intLineCounter = 0

    theByte1 = file.read(1)

file.close()

file = open(outputfilename, "w")
file.write(strNewFile)
file.close()
