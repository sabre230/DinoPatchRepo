import traceback
from os import path
from os import getcwd
from os.path import exists

READ_PATH = "dinomod24.z64" # ROM file to copy bytes to
WRITE_PATH = "newpatch.z64" # Output file

def miscPatches(buffer):
    #Map Layer Patches
    writeWord(buffer, 0x38E1E14, 0) #Revert Dinomod's flawed DIM void spawn patch

    writeWord(buffer, 0x039BF768, 0)
    writeWord(buffer, 0x039BF778, 0x01A02025)
    writeWord(buffer, 0x00047F7C, 0xA0440000)
    writeWord(buffer, 0x00047F88, 0)
    writeByte(buffer, 0x020E21FC, 255)
    writeByte(buffer, 0x020E2200, 0)
    writeByte(buffer, 0x02102830, 255)
    writeByte(buffer, 0x02102834, 0)
    writeByte(buffer, 0x0210FA4C, 255)
    writeByte(buffer, 0x0210FA50, 0)
    writeByte(buffer, 0x021200E8, 255)
    writeByte(buffer, 0x021200EC, 0)
    writeByte(buffer, 0x0212017C, 255)
    writeByte(buffer, 0x02120180, 0)
    writeByte(buffer, 0x021218F0, 255)
    writeByte(buffer, 0x02138854, 0)
    writeByte(buffer, 0x02138858, 255)
    writeByte(buffer, 0x02138990, 0)
    writeByte(buffer, 0x021389E0, 254)
    writeByte(buffer, 0x021439F4, 255)
    writeByte(buffer, 0x021439F8, 0)
    writeByte(buffer, 0x02143E88, 255)
    writeByte(buffer, 0x02143E8C, 0)
    writeByte(buffer, 0x02143ED8, 255)
    writeByte(buffer, 0x02143EDC, 0)
    writeByte(buffer, 0x02144880, 255)
    writeByte(buffer, 0x02144884, 0)
    writeByte(buffer, 0x0215258C, 1)
    writeByte(buffer, 0x02152590, 2)
    writeByte(buffer, 0x021532B4, 0)
    writeByte(buffer, 0x021532B8, 1)
    writeByte(buffer, 0x02188C88, 0)
    writeByte(buffer, 0x02188CD8, 0)
    writeByte(buffer, 0x0218D464, 255)
    writeByte(buffer, 0x0218D468, 0)
    writeByte(buffer, 0x0218FF20, 0)
    writeByte(buffer, 0x0218FF24, 255)
    writeByte(buffer, 0x02190040, 0)
    writeByte(buffer, 0x02190044, 255)
    writeByte(buffer, 0x02190530, 0)
    writeByte(buffer, 0x02190534, 255)
    writeByte(buffer, 0x021907EC, 255)
    writeByte(buffer, 0x021907F0, 0)
    
    #New checksum, I suggest you use rn64crc.exe instead for this if you can.
    #https://www.smwcentral.net/?p=section&a=details&id=8799
    writeBytes(buffer,0x00000010, "88 50 D3 CE EF 76 29 DC")

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

