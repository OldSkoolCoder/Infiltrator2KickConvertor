import sys, getopt

# To run this program use this command 
# python3 ConvertINFILTRATORFileToASM.py --input=Filename --output=Filename

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

full_cmd_arguments = sys.argv

# Keep all but the first
argument_list = full_cmd_arguments[1:]

#print (argument_list)

short_options = "hi:o:"
long_options = ["help", "input=", "output="]

inputfilename = ""
outputfilename = ""

#-------------------------------------------------------------------
# Added By C64Mark
SCREENRAM = 0x4400
COLOURRAM = 0xD800

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

# text file should be in the format e.g. $D000,SPRX0\n
# Added By C64Mark
#-------------------------------------------------------------------
file = open("IO.map", "r")

IOMap = []

for tmp in file:
    tmp = tmp.replace("\n","")
    tmp = tmp.split(",")
    IOMap.append(tmp)

file.close()
#-------------------------------------------------------------------

file = open(inputfilename, "r")

strNewFile = ""
strNewLine = ""
intLineCounter = 0
intSpriteCounter = 0

strtheLine = file.readline()
while strtheLine:

    strtheLine = strtheLine.replace("\n","")
    if left(strtheLine,1) == "$":
        strtheLine = "\t" + mid(strtheLine,17,3).lower() + strtheLine.replace(left(strtheLine,20),"")

        if mid(strtheLine,1,3) in ["jmp","jsr","bne","beq","bcc","bcs","bvc","bvs","bpl","bmi"]:
            if mid(strtheLine,5,2) == "L_":
                strtheLine = strtheLine.replace(")_","_")
                strtheLine = strtheLine.replace(") ","_")
                strtheLine = strtheLine.replace("_($","_")
            
        elif mid(strtheLine,1,3) in ["asl","rol","lsr","ror"]:
            strtheLine = strtheLine.replace(" A","")

    elif left(strtheLine,2) == "L_":
        strtheLine += ":"
        strtheLine = strtheLine.replace("$","")
        strtheLine = strtheLine.replace(") ","_")
        strtheLine = strtheLine.replace(")","")
        strtheLine = strtheLine.replace("(","")

#-------------------------------------------------------------------
# Added By C64Mark
    if mid(strtheLine,5,1) == "$":
        tmp = int(mid(strtheLine,6,4), 16)
        if tmp >= SCREENRAM and tmp <(SCREENRAM+1000):
            tmp = hex(tmp - SCREENRAM)
            tmp = right(tmp, len(tmp)-2)
            tmp = left(strtheLine, 5) + "SCREENRAM+$" + tmp.zfill(3).upper()
            if mid(strtheLine,10,1) == ",":
                tmp = tmp + mid(strtheLine,10,2)
            strtheLine = tmp 
 
        elif tmp >= COLOURRAM and tmp <(COLOURRAM+1000):
            tmp = hex(tmp - COLOURRAM)
            tmp = right(tmp, len(tmp)-2)
            tmp = left(strtheLine, 5) + "COLOURRAM+$" + tmp.zfill(3).upper()
            if mid(strtheLine,10,1) == ",":
                tmp = tmp + mid(strtheLine,10,2)
            strtheLine = tmp       

#-------------------------------------------------------------------
# Added By C64Mark
    # based on tuples in IO.txt file
    for i, o in IOMap:
        strtheLine = strtheLine.replace(i, o)
#-------------------------------------------------------------------

    strNewFile += strtheLine + "\n"

    strtheLine = file.readline()

file.close()

file = open(outputfilename, "w")
file.write(strNewFile)
file.close()
