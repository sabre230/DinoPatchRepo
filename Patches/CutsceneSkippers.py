import traceback
from os import path

READ_PATH = "dinomod24.z64" #Source file to merge with
WRITE_PATH = "newpatch.z64" #Output

def miscPatches(buffer):
    writeHalfWord(buffer, 0x037E6F4E, 0x0800) # "Sharpclaw picks up barrel, explodes, and other Sharpclaw laugh" (DF)
    writeHalfWord(buffer, 0x037E6FA6, 0x0800) # "Kyte using Discovery Falls lever to activate lift platforms" (DF)
    writeHalfWord(buffer, 0x037E70D6, 0x0800) # "Take me to Warlock Mountain" (DF)
    writeHalfWord(buffer, 0x037E743E, 0x0800) # "My name is Sabre, Royal Knight from the planet Animus" (IM)
    writeHalfWord(buffer, 0x037E748E, 0x0800) # "Kyte
    writeHalfWord(buffer, 0x037E757E, 0x0800) # "Lightfoot
    writeHalfWord(buffer, 0x037E762E, 0x0800) # "LightFoot Dives in water, drains entrance to Discovery Falls" (SC)
    writeHalfWord(buffer, 0x037E7656, 0x0800) # "Golden Plains statue enter 1" (GP)
    writeHalfWord(buffer, 0x037E76A6, 0x0800) # "Lightfoot
    writeHalfWord(buffer, 0x037E7C1E, 0x0800) # "Queen
    writeHalfWord(buffer, 0x037E7C5E, 0x0800) # "QEarthwalker
    writeHalfWord(buffer, 0x037E7D96, 0x0800) # "Fox falls into Hot Spring after race" (IM)
    writeHalfWord(buffer, 0x037E7FB6, 0x0800) # "I am forever in your debt (Flame command)" (DIM)
    writeHalfWord(buffer, 0x037E801E, 0x0800) # Test of Combat pass (DFSH)
    writeHalfWord(buffer, 0x037E8186, 0x0800) # Test of Fear pass (MMSH)
    writeHalfWord(buffer, 0x037E827E, 0x0800) # Test of Skill pass (ECSH)
    writeHalfWord(buffer, 0x037E8376, 0x0800) # "Garunda Te
    writeHalfWord(buffer, 0x037E83CE, 0x0800) # "Garunda Te
    writeHalfWord(buffer, 0x037E85D6, 0x0800) # Test of Knowledge pass (GPSH)
    writeHalfWord(buffer, 0x037E86C6, 0x0800) # Test of Strength pass (DBSH)
    writeHalfWord(buffer, 0x037E87AE, 0x0800) # Test of Sacrifice pass (NWSH)
    writeHalfWord(buffer, 0x037E88C6, 0x0800) # Test of Character pass (CCSH)
    writeHalfWord(buffer, 0x037E8996, 0x0800) # Test of Magic pass (WGSH)
    writeHalfWord(buffer, 0x037E8BFE, 0x0800) # "So this is Discovery Falls!" (DF)
    writeHalfWord(buffer, 0x037E8C26, 0x0800) # "Hightop
    writeHalfWord(buffer, 0x037E8CA6, 0x0800) # "Who're you? My name is Belina Te" (DIM2)
    writeHalfWord(buffer, 0x037E8DB6, 0x0800) # "This, is Cloudrunner Fortress!" (CF)
    writeHalfWord(buffer, 0x037E8DDE, 0x0800) # "I have a feeling Scales isn't doing this alone) (CF)
    writeHalfWord(buffer, 0x037E9096, 0x0800) # "Fox you made it! (Belina)" (DIM2)
    writeHalfWord(buffer, 0x037E90FE, 0x0800) # "Greetings stranger, my name is Rubble (Krystal 1st SC visit)" (SC)
    writeHalfWord(buffer, 0x037E9126, 0x0800) # "Are you lost little one?" (SC)
    writeHalfWord(buffer, 0x037E952E, 0x0800) # "Did you find the guardian yet? (Distract command)" (CF)
    writeHalfWord(buffer, 0x037E982E, 0x0800) # "When this is all over I must return to rule as Queen" (CF)
    writeHalfWord(buffer, 0x037E9A0E, 0x0800) # "Diamond Bay Intro" (DB)
    writeHalfWord(buffer, 0x037E9BD6, 0x0800) # "Are you ok? What sort of Dinosaur are you? (Forcefield spell) (CC)
    writeHalfWord(buffer, 0x037EA116, 0x0800) # "Sabre
    writeHalfWord(buffer, 0x037EA136, 0x0800) # "QEarthwalker
    writeHalfWord(buffer, 0x037EA216, 0x0800) # "QEarthwalker
    writeHalfWord(buffer, 0x037EA236, 0x0800) # "QEarthwalker
    writeHalfWord(buffer, 0x037EA51E, 0x0800) # "Do not hit Sharpclaw! (food bag given)" (DF)
    writeHalfWord(buffer, 0x037EA696, 0x0800) # "Skeetlas! C'mon Tricky we gotta help him!" (DR)
    writeHalfWord(buffer, 0x037EA95E, 0x0800) # "Boss Klanadack Intro" KTRexSequences
    writeHalfWord(buffer, 0x037EAAD6, 0x0800) # "Garunda Te
    writeHalfWord(buffer, 0x037EAB06, 0x0800) # "Garunda Te
    writeHalfWord(buffer, 0x037EAE3E, 0x0800) # Lightfoot gives Krystal MMP key "I made a promise the Cloudrunner could get home" SC
    writeHalfWord(buffer, 0x037EAF2E, 0x0800) # "Ah hello again Krystal, and welcome to Golden Plains" GP
    writeHalfWord(buffer, 0x037EB00E, 0x0800) # Cloudrunner
    writeHalfWord(buffer, 0x037EB2EE, 0x0800) # "Krystal! It's the Spellstone holder!" (DFP1)
    writeHalfWord(buffer, 0x037EB406, 0x0800) # "In the dark of the tree hollow" GP
    writeHalfWord(buffer, 0x037EC456, 0x0800) # "I can taste your fear animal" (KD)
    writeHalfWord(buffer, 0x037ECE16, 0x0800) # "Entering Golden Plains via statue" (SC)

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
    
    script_path = path.dirname(path.realpath(__file__)) + "\\"
    READ_PATH = script_path + READ_PATH
    WRITE_PATH = script_path + WRITE_PATH
    print("Script Directory:", script_path)
    
    OLD_READ_PATH = READ_PATH
    if path.exists(READ_PATH):
        print(READ_PATH + " found!")
    else:
        READ_PATH += ".z64"

    if not path.exists(READ_PATH):
        print("ERROR:", OLD_READ_PATH + " is missing! Is it named correctly?")
        input("")
        return

    print("Rom location:", READ_PATH)
    print("Patch location:", WRITE_PATH)

    test = input("Enter '1' to confirm patch.\n")
    if test == "1" or test == "'1'":
        print("Please wait...")
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

