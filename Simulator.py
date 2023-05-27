#CO Simulator
#Vaibhav Gupta
#Vaibhav Sehara

def TypeA(code):
        #"5bit opcode"+ "2 Unused bit"+"3 reg of 3 bit each"
        opcode = ""
        for i in range(0,5):
            opcode+=code[i]
        r1 = ""
        r2 = ""
        r3 =""
        for i in range(7,10):
            r1 += code[i]
        for i in range(10,13):
            r2 += code[i]
        for i in range(13,16):
            r3 += code[i]
        list = [opcode,r1,r2,r3]
        return list
def TypeB(code):
    # "5bit opcode"+ "1 Unused bit"+"1 reg of 3 bit "+ "7 bit Immediate value"
    opcode = ""
    for i in range(0, 5):
        opcode += code[i]
    r1 = ""
    imm = ""
    for i in range(6, 9):
        r1 += code[i]
    for i in range(9, 16):
        imm += code[i]
    list = [opcode, r1, imm]
    return list
def TypeC(code):
    # "5bit opcode"+ "5 unused"+"2 reg of 3 bit each"
    opcode = ""
    for i in range(0, 5):
        opcode += code[i]
    r1 = ""
    r2 = ""
    for i in range(10, 13):
        r1 += code[i]
    for i in range(13, 16):
        r2 += code[i]
    list = [opcode, r1, r2]
    return list
def typeD(code):
    # "5bit opcode"+ "1 Unused bit"+"1 reg of 3 bit "+ "mem_addr"
    opcode = ""
    for i in range(0, 5):
        opcode += code[i]
    r1 = ""
    mem_addr = ""
    for i in range(6, 9):
        r1 += code[i]
    for i in range(9, 16):
        mem_addr += code[i]
    list = [opcode, r1, mem_addr]
    return list
def TypeE(code):
    #"5 bit opcode" + "4 unused" + "7 mem_addr"
    opcode = ""
    for i in range(0,5):
        opcode += code[i]
    mem_addr=""
    for i in range(9,16):
        mem_addr+=code[i]
    list = [opcode,mem_addr]
    return list
def TypeF(code):
    #"5 bit opcode" + "11 UNUSED   "
    opcode = ""
    for i in range(0,5):
        opcode += code[i]
    list = [opcode]
    return list

