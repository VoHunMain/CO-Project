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
def TypeD(code):
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

#-------------------------------------- 

#registers
registers = ["0000000000000000"] * 7  # R0 to R6

#flags
flag = [0] * 4  # V L G E

#memory
memory = ['0000000000000000']*256

#program counter
pc = 0

def add(code):
    r1 = code[7:10]
    r2 = code[10:13]
    r3 = code[13:]

    flag[0] =  flag[1] = flag[2] =  flag[3] = 0   # Reset flags register

    sum = int(registers[int(r2)], 2) + int(registers[int(r3)], 2)
    # Checking for overflow
    if sum > (2 ** 16) - 1:
        flag[0] = 1  # Overflow bit set if overflow occurs
        registers[r1] = bin(sum & 0xFFFF)[-16:] 
        #0xFFFF to mask off the upper bits, we ensure that the  result is limited to 16 bits and can be safely stored in a 16-bit register.
    else:
        temp = bin(sum)[2:]
        registers[r1] = '0' * (16 - len(temp)) + temp
    
    pc += 1  # Increment program counter
    
    return (1, False)


def sub(code):
    r1 = code[7:10]
    r2 = code[10:13]
    r3 = code[13:]

    flag[0] = flag[1] = flag[2] = flag[3] = 0  # Reset flags register

    difference = int(registers[int(r2)], 2) - int(registers[int(r3)], 2)
    # Checking for underflow
    if difference < 0:
        flag[0] = 1  # Underflow bit set if underflow occurs
        registers[r1] = bin(difference & 0xFFFF)[-16:]  # making sure result of substraction is less than 16 bit.
    else:
        temp = bin(difference)[2:]
        registers[r1] = '0' * (16 - len(temp)) + temp

    pc += 1  # Increment program counter

    return (1, False)

def mul(code):
    r1 = code[7:10]
    r2 = code[10:13]
    r3 = code[13:]

    flag[0] = flag[1] = flag[2] = flag[3] = 0  # Reset flags register

    product = int(registers[int(r2)], 2) * int(registers[int(r3)], 2)
    # Checking for overflow
    # 2^16 - 1  =  1111111111111111 in binary. so, if the integer value of product is greater than integer value of maximum binary, then the binary value will also be greater.
    if product > (2 ** 16) - 1: 
        flag[0] = 1  # Overflow bit set if overflow occurs
        registers[r1] = bin(product & 0xFFFF)[-16:]  
    else:
        temp = bin(product)[2:]
        registers[r1] = '0' * (16 - len(temp)) + temp

    pc += 1  # Increment program counter

    return (1, False)
