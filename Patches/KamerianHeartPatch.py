import traceback
from os import path
from os import getcwd
from os.path import exists

READ_PATH = "dinomod24.z64" # ROM file to copy bytes to
WRITE_PATH = "newpatch.z64" # Output file

def miscPatches(buffer):
    #-------------- KD Map Blocks Patch --------------
    writeWord(buffer, 0x02002CDC, 0xFFFDFFF4) #Position
    writeHalfWord(buffer, 0x02002CE0, 0x00FF) # Map Layer
    #writeHalfWord(buffer, 0x02194192, 0x000E) #Nurse to animator (optional)
    #Nulling 0500, and 0502 here will help load the bottom two KD blocks
    writeHalfWord(buffer, 0x218F6F6, 0x1FFE)
    writeHalfWord(buffer, 0x218F6FA, 0x1FFE)
    #Kamerian loading block sizes
    writeByte(buffer, 0x02193DAD, 0x89)
    writeByte(buffer, 0x02193DB5, 0x79)
    writeByte(buffer, 0x02193DBD, 0x89)
    writeByte(buffer, 0x02193DC5, 0x79)
    writeByte(buffer, 0x02193DCD, 0x89)
    writeByte(buffer, 0x02193DD5, 0x89)
    writeByte(buffer, 0x02193DDD, 0x89)
    writeByte(buffer, 0x02193DE5, 0x89)
    writeByte(buffer, 0x02193DF5, 0x89)
    writeByte(buffer, 0x02193DFD, 0x89)
    writeByte(buffer, 0x02193E05, 0x79)
    writeByte(buffer, 0x02193E0D, 0x89)
    writeByte(buffer, 0x02193E15, 0x79)
    writeByte(buffer, 0x02193E1D, 0x89)
    writeByte(buffer, 0x02193E25, 0x89)
    writeByte(buffer, 0x02193E2D, 0x89)
    writeByte(buffer, 0x02193E35, 0x89)
    writeByte(buffer, 0x02193E45, 0x89)

def writeHalfWord(buffer, offset, val):
    writeByte(buffer, offset, (val >> 8) & 255)
    writeByte(buffer, offset+1, val & 255)

def writeString(buffer, offset, val):
    for i in range(len(val)):
        writeByte(buffer, offset+i, ord(val[i]))

def writeByte(buffer, offset, val):
    if patches.get(offset) != None:
        print("WARNING: %08X" % offset + " is already used!")
        traceback.print_stack(limit=4, file=None)
    buffer[offset] = val
    patches[offset] = val
    
def writeBytesNoSpaces(buffer, offset, val):
    n = 0
    for i in range(0,len(val),2):
        byte = int(val[i:i+2],16)
        writeByte(buffer, offset+n, byte)
        n+=1

def writeWord(buffer, offset, val):
    writeByte(buffer, offset, (val>>24)&255)
    writeByte(buffer, offset+1, (val>>16)&255)
    writeByte(buffer, offset+2, (val>>8)&255)
    writeByte(buffer, offset+3, (val&255))

def writeBytes(buffer, offset, val):
    n = 0
    for i in range(0,len(val),3):
        byte = int(val[i:i+2],16)
        writeByte(buffer, offset+n, byte)
        n+=1

def patchROM():
    global READ_PATH, WRITE_PATH, patches
    
    script_path = path.dirname(path.realpath(__file__))+"\\"
    READ_PATH = script_path+READ_PATH
    WRITE_PATH = script_path+WRITE_PATH

    #print("Working Directory:", getcwd())
    print("Script Directory:", script_path)
    
    OLD_READ_PATH = READ_PATH
    if exists(READ_PATH):
        print(READ_PATH + " found!")
    else:
        READ_PATH += ".z64"

    if not exists(READ_PATH):
        print("ERROR:", OLD_READ_PATH + " is missing! Is it named correctly?")
        input("")
        return

    print("Rom location:", READ_PATH)
    print("Patch location:", WRITE_PATH)

    test = input("Enter '1' to confirm patch.\n")
    if test == "1" or test == "'1'":
        patches = {}
        file = open(READ_PATH,"rb")
        buffer = list(file.read())
        file.close()
        miscPatches(buffer)
        file = open(WRITE_PATH,"wb")
        file.write(bytes(buffer))
        file.close()
        
        print("PATCHED!")
    else:
        print("Invalid option.")

patchROM()

