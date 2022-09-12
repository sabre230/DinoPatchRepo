import traceback
from os import path
from os import getcwd
from os.path import exists

READ_PATH = "dinomod24.z64" # ROM file to copy bytes to
WRITE_PATH = "newpatch.z64" # Output file

def miscPatches(buffer):
    #Item pickup fixes 05-11-2022
    writeHalfWord(buffer, 0x037F68B8, 0x043D) #CFPrisonKey
    writeHalfWord(buffer, 0x037F8A04, 0x00DB) #CFPowerCrystal1
    writeHalfWord(buffer, 0x037F8ADC, 0x00E1) #CFPowerCrystal2
    writeHalfWord(buffer, 0x037F8BB4, 0x00E2) #CFPowerCrystal3
    writeHalfWord(buffer, 0x037FA498, 0x0363) #CFPowerRoomKey
    writeHalfWord(buffer, 0x037FA7AC, 0x043D) #CFExplosiveKey
    writeHalfWord(buffer, 0x037FD514, 0x052C) #WCSunStone
    writeHalfWord(buffer, 0x037FD5EC, 0x052D) #WCMoonStone
    writeHalfWord(buffer, 0x037FD7A0, 0x052B) #WCTrexTooth
    writeHalfWord(buffer, 0x037FEA88, 0x0213) #DIMBridgeCogCol
    writeHalfWord(buffer, 0x037FF588, 0x043D) #DIMShackleKey
    writeHalfWord(buffer, 0x037FFE60, 0x0250) #DIMAlpineRoot
    writeHalfWord(buffer, 0x037FFF38, 0x0250) #DIMAlpineRoot2
    writeHalfWord(buffer, 0x03800B10, 0x031A) #DIMTruthHorn
    writeHalfWord(buffer, 0x038013A8, 0x043D) #DIM2CellKey
    writeHalfWord(buffer, 0x03801D18, 0x043D) #DIM2SilverKey
    writeHalfWord(buffer, 0x03801DF0, 0x043D) #DIM2GoldKey
    writeHalfWord(buffer, 0x038023CC, 0x043D) #DIM2PuzzleKey
    writeHalfWord(buffer, 0x038032D8, 0x0361) #PortalSpell
    writeHalfWord(buffer, 0x038053C8, 0x043D) #CCCellKey
    writeHalfWord(buffer, 0x03806F84, 0x02E5) #CCgoldnuggetPic
    writeHalfWord(buffer, 0x03809CEC, 0x05BA) #NWtrickyball
    writeHalfWord(buffer, 0x03809DC4, 0x018B) #NWalpineroot
    writeHalfWord(buffer, 0x0380A954, 0x05B0) #NWreplaymedal
    writeHalfWord(buffer, 0x03813E60, 0x0392) #WMconsolestone
    writeHalfWord(buffer, 0x03814568, 0x05B0) #WM_PureMagic
    writeHalfWord(buffer, 0x03826D08, 0x0446) #meatPickup
    writeHalfWord(buffer, 0x03826DC8, 0x0444) #applePickup
    writeHalfWord(buffer, 0x03826E88, 0x0445) #beanPickup
    writeHalfWord(buffer, 0x03826F48, 0x043D) #PadlockKey
    writeHalfWord(buffer, 0x03827008, 0x05B0) #GuardPass
    writeHalfWord(buffer, 0x038270C8, 0x05B0) #Dynamite
    writeHalfWord(buffer, 0x03827188, 0x05B0) #BoneDust
    writeHalfWord(buffer, 0x03827260, 0x0392) #Spellstone
    writeHalfWord(buffer, 0x03827338, 0x0361) #ProjectileSpell
    writeHalfWord(buffer, 0x03827410, 0x0361) #IllusionSpell
    writeHalfWord(buffer, 0x038274E8, 0x0361) #FireSpell
    writeHalfWord(buffer, 0x038275C0, 0x0361) #EarthQuakSpell
    writeHalfWord(buffer, 0x03827680, 0x05B0) #WeaponUp
    writeHalfWord(buffer, 0x03827A48, 0x05B0) #foodbagSmall
    writeHalfWord(buffer, 0x03827B20, 0x05B0) #foodbagMedium
    writeHalfWord(buffer, 0x03827BF8, 0x05B0) #foodbagLarge
    writeHalfWord(buffer, 0x03829458, 0x05B0) #FireNut
    writeHalfWord(buffer, 0x03829800, 0x05B0) #fishingnetColle

def writeHalfWord(buffer, offset, val):
    writeByte(buffer, offset, (val >> 8) & 255)
    writeByte(buffer, offset+1, val & 255)

def writeByte(buffer, offset, val):
    if patches.get(offset) != None:
        print("WARNING: %08X" % offset + " is already used!")
        traceback.print_stack(limit=4, file=None)
    buffer[offset] = val
    patches[offset] = val

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

