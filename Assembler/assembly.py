# co project
# Vaibhav Gupta
# Vaibhav Sehara

# global variable FLAGS and binary_code.
registers = ["0000000000000000"] * 7  # R0 to R6
mem_addr ={}
flag = [0] * 4  # V L G E
binary_code = []


# TYPE - A -START

# Opcode(5 bits)  Unused(2 bits)   reg1(3 bits)   reg2(3 bits)   reg3(3 bits)
def add(x, y, z):
    # Performs reg1 =reg2 + reg3.If the computation overflows, then the overflow flag is set and 0 is written in reg1
    # get binary values of functions
    global flag
    adds = int(str(registers[int(y[1])]), 2) + int(str(registers[int(z[1])]), 2)
    # Check for overflow
    if int(str(registers[int(y[1])]), 2) + int(str(registers[int(z[1])]), 2) > int("1" * 16, 2):
        flag[0] = 1  # Set V flag if overflow occurs
    else:
        flag[0] = 0  # Clear V flag if no overflow occurs

    # Add values in y and z registers and store in x register
    registers[int(x[1])] = bin(adds)[2:].zfill(16)

    binary_code.append(opcode["add"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def sub(x, y, z):
    # Performs reg1 = reg2 + reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1

    subs = int(str(registers[int(y[1])]), 2) - int(str(registers[int(z[1])]), 2)

    # check if subtraction will result in overflow
    if int(str(registers[int(z[1])]), 2) > int(str(registers[int(y[1])]), 2):
        flag[0] = 1
        registers[int(x[1])] = "0000000000000000"
    else:
        flag[0] = 0
        registers[int(x[1])] = bin(subs)[2:].zfill(16)

    # update register value and append binary code to list

    binary_code.append(str(opcode["sub"][0] + "00" + str(reg_code[x]) + str(reg_code[y]) + str(reg_code[z])))


def mul(x, y, z):
    # Performs reg1 = reg2 x reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1
    # checking for overflow and setting FLAG.
    mult = 0
    mult = int(str(registers[int(y[1])]), 2) * int(str(registers[int(z[1])]), 2)
    if mult > int("1" * 16, 2):
        flag[0] = "1"  # Set V flag if overflow occurs
        # registers[x] = "0000000000000000"  # Set reg1 to 0
    else:
        flag[0] = "0"  # Clear V flag if no overflow
        registers[int(x[1])] = bin(mult)[2:].zfill(16)

    binary_code.append(opcode["mul"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def Or(x, y, z):
    # Performs bitwise OR of reg2 and reg3. Stores the result in reg1.

    binary_code.append(opcode["or"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def xor(x, y, z):
    # Performs bitwise XOR of reg2 and reg3. Stores the result in reg1.

    binary_code.append(opcode["xor"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def And(x, y, z):
    ## Appending the opcode of and instruction along with the syntax supposed for the and instruction

    binary_code.append(opcode["and"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


# TYPE A - END

# - --- ---- ----- ----------- ---------------- ---------- ----------------- ---------- --------- ------------- -------- ---------- -----------------------------

# TYPE - B - START

# Opcode(5 bits)  Unused(1 bit)   reg1(3 bits)   Immediate value(7 bits)

def mov_imm(x, y):
    binary = bin(int(y))  # ---------> covert string to binary by removing the 0b.

    if (len(binary[2:]) < 8):  ##CHECKING IF LENGTH OF binary less than 8
        extras = 7 - len(binary[2:])  ##Adding extra zeroes if required
        imm = str("0" * extras) + binary[2:]
        registers[int(x[1])] = "000000000"+str(imm)
    else:
        registers[int(x[1])]="".zfill(16)
    binary_code.append(
        str(opcode["mov"][0][0]) +"0" +str(reg_code[x]) + str(imm))  ## mov [0][0], as we have 2 "mov" function.


def RightShift(x, y):
    # Right shifts reg1 by $Imm, where $Imm is a 7 bit value.

    binary = bin(int(y[1:]))  # ---------> covert string to binary by removing the 0b.

    if (len(binary[2:]) < 8):  ##CHECKING IF LENGTH OF binary less than 8
        extras = 8 - len(binary[2:])
        imm = str("0" * extras) + binary[2:]
    else:
        imm = binary[2:]

    # value = int(registers[x], 2)  # get current value in register x
    # new_value = value >> imm  # perform the right shift operation
    # registers[x] = format(new_value, '016b')  # store the new value in register x

    binary_code.append(opcode["rs"][0] + "0"+reg_code[x] + y[1:].zfill(7))


def LeftShift(x, y):
    # Left shifts reg1 by $Imm, where $Imm is a 7 bit value.

    binary = bin(int(y[1:]))  # ---------> covert string to binary by removing the 0b.

    if (len(binary[2:]) < 8):  # CHECKING IF LENGTH OF binary less than 8
        extras = 8 - len(binary[2:])
        imm = str("0" * extras) + binary[2:]
    else:
        imm = binary[2:]

    binary_code.append(opcode["ls"][0] + reg_code[x] + imm)


##TYPE B ends

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

##TYPE C starts


def MovReg(x, y):
    # Move content of reg2 into reg1.
    cont1 = registers[int(y[1])]
    registers[int(x[1])]=cont1
    registers[int(y[1])] = "0"*16
    binary_code.append(opcode["mov"][1][0] + "00000" + reg_code[x] + reg_code[y])

# Initialize R0 and R1 to 0
# reg["R0"] = 0
# reg["R1"] = 0

def div(x, y):
    # Performs reg3/reg4. Stores the quotient in R0 and the remainder in R1.
    # If reg4 is 0 then overflow flag is set and content of R0 and R1 are set to 0

    # if  y == 0:
    #     # set overflow flag and clear R0 and R1
    #     flag[0] = 1
    #     reg["R0"] = 0
    #     reg["R1"] = 0
    # else:
    #     # perform division
    #     quotient = registers[int(x[1])] // registers[int(y[1])]
    #     remainder = registers[int(x[1])] %  registers[int(y[1])]
    #     # store quotient in R0 and remainder in R1
    #     reg["R0"] = quotient
    #     reg["R1"] = remainder


    binary_code.append(opcode["div"][0] + "00000" + reg_code[x] + reg_code[y])


def Invert(x, y):
    # Performs bitwise NOT of reg2. Stores the result in reg1.

    binary_code.append(opcode["not"][0] + "00000" + reg_code[x] + reg_code[y])


def Compare(x, y):
    # Compares reg1 and reg2 and sets up the FLAGS register.

    global flag

    val_x = int(registers[x], 2)
    val_y = int(registers[y], 2)

    # Set L flag if val_x < val_y
    if val_x < val_y:
        flag[1] = 1
    else:
        flag[1] = 0

    # Set G flag if val_x > val_y
    if val_x > val_y:
        flag[2] = 1
    else:
        flag[2] = 0
    # Set E flag if val_x == val_y
    if val_x == val_y:
        flag[3] = 1
    else:
        flag[3] = 0

    binary_code.append(opcode["cmp"][0] + "00000" + reg_code[x] + reg_code[y])


# TYPE C ends

# TYPE D starts here

# def load(x, y):
#     # Loads data from mem_addr into reg1.
#     if (len(binary[2:] < 8)):
#         extras = 8 - len(binary[2:])  ##Adding extra zeroes if required
#         imm = str("0" * extras) + binary[2:]
#     else:
#         imm = binary[2:]
#
#     binary_code.append(opcode["ld"][0] + "00000" + reg_code[x] + imm)


def store(x, y):
    # Stores data from reg1 to mem_addr.

    if (len(y) < 8):
        extras = 7 - len(y)  ##Adding extra zeroes if required
        imm = str("0" * extras) + y
    else:
        imm = binary[2:]

    binary_code.append(opcode["st"[0] + "00000" + reg_code[x] + imm])


# TYPE D ENDS HERE

# TYPE E STARTS HERE

def unconditional_jump(address):
    # Jumps to mem_addr, where mem_addr is a memory address.

    binary = bin(address)

    if (len(binary[2:]) < 8):
        extras = 7 - len(binary[2:])  ##Adding extra zeroes
        imm = str(str("0" * extras) + binary[2:])
    else:
        imm = str(binary[2:])

    binary_code.append(opcode["jmp"[0]] + "0000" + str(imm))


def jumpifless(address):
    # Jump to mem_addr if the less than flag is set (less than flag = 1), where mem_addr is a memory address.

    binary = bin(address)

    if (len(binary[2:]) < 8):
        extras = 7 - len(binary[2:])  ##Adding extra zeroes
        imm = str(str("0" * extras) + binary[2:])
    else:
        imm = str(binary[2:])

    binary_code.append(opcode["jlt"][0] + "0000" + imm)


def jumpifgreater(address):
    # Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address.

    binary = bin(address)

    if (len(binary[2:]) < 8):
        extras = 7 - len(binary[2:])  ##Adding extra zeroes
        imm = str(str("0" * extras) + binary[2:])
    else:
        imm = str(binary[2:])

    binary_code.append(opcode["jgt"][0] + "0000" + str(imm))


def jumpifequal(address):
    # Jump to mem_addr if the equal flag is set (equal flag = 1), where mem_addr is a memory address.

    binary = bin(address)

    if (len(binary[2:]) < 8):
        extras = 7 - len(binary[2:])  ##Adding extra zeroes
        imm = str("0" * extras) + binary[2:]
    else:
        imm = binary[2:]

    binary_code.append(opcode["je"][0] + "0000" + str(imm))


# TYPE E ENDS HERE

# TYPE F STARTS HERE

def halt():
    binary_code.append(opcode["hlt"[0] + "0" * 11])
# TYPE F ENDS HERE


blank_count = 0
msg = ""
isthere = False
opcode = {"add": ("00000", "A"), "sub": ("00001", "A"), "mov": (("00010", "B"), ("00011", "C"))
    , "ld": ("00100", "D"), "st": ("00101", "D"), "mul": ("00110", "A"), "div": ("00111", "C"),
          "rs": ("01000", "B"), "ls": ("01001", "B"), "xor": ("01010", "A"), "or": ("01011", "A"),
          "and": ("01100", "A"),
          "not": ("01101", "C"), "cmp": ("01110", "C"), "jmp": ("01111", "E"), "jlt": ("11100", "E"),
          "jgt": ("11101", 'E'), "je": ("11111", 'E'),
          "hlt": ("11010", "F")}
ocv = ["ld", "st"]


def variable_index(line):
    ind = 0
    if line[0] in ocv:
        if line[0] == "ld" or line[0] == "st":
            ind = 2
    return ind


inst = []
reg = []
label = []
for j in opcode:
    inst.append(j)
reg_code = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110',
            'FLAGS': '111'}
for j in reg_code:
    reg.append(j)
f = open("opcode.txt", "r")
f3 = open("binary_file.txt", "w")
vari = []
for lines in f:
    l2 = lines.split()
    if l2[0] == "var":
        vari.append(l2[1])
f2 = open("error_file.txt", "w")
f.close()
# creating a list to add each line of assembly instruction as an element of this list
f = open("opcode.txt", "r")
instructions = []
for line in f:
    l = line.strip()
    instructions.append(l)
dict = {}
# -----------------------------------------------
correct = True
# Now beggining the check if the given assembly code is correct or not:
for i in instructions:
    l1 = str(i).split(" ")
    s = ""
    for o in range(len(l1)):
        if l1[0][len(l1[0]) - 1] == ":":
            for k in range(0, len(l1[0]) - 1):
                s += l1[0][k]
            label.append(s)
    # -----------------------------------------------

    # Checking part a: Typos in instruction name or register name
    # checking for the initial instruction
    if l1[0] not in inst and l1[0] != "var" and l1[0][len(l1[0]) - 1] != ":":
        correct = False
        f2.write(
            "There is a typing error in the instruction name in line number " + str(instructions.index(i) + 1) + "\n")

    # -----------------------------------------------

    # now checking the typo in register name
    for m in range(len(l1)):
        if l1[m][0] == "R" and l1[0] != "var" and m not in vari:
            if l1[m] not in reg:
                correct = False
                f2.write("There is a typing error in the register name in line number " + str(
                    instructions.index(i) + 1) + "\n")

    # -----------------------------------------------

    # now checking any use of undefined variable
    if l1[0] in ocv:
        if l1[variable_index(l1)] not in vari:
            correct = False
            f2.write("The variable " + l1[variable_index(l1)] + " used in line " + str(
                instructions.index(i) + 1) + " is undefined " + "\n")

    # -----------------------------------------------

    # checking that all the variables are declared at the starting of the assembly code
    lines = []
    for l in range(1, len(instructions)):
        l2 = instructions[l].split(" ")
        if l2[0] == "var":
            for z in range(0, l):
                if instructions[z].split(" ")[0] != "var":
                    lines.append(l + 1)
    liney = set(lines)
    if len(liney) != 0:
        correct = False
    # -----------------------------------------------
    # Checking the misuse of labels as variables or vice versa

    # -----------------------------------------------

    # now checking any undefined labels in the code
    po = ["jmp", "jlt", "jgt", "je"]
    if l1[0] in po:
        dict.update({l1[1]: [0, instructions.index(i) + 1]})
    for j in dict:
        if j in label:
            dict[j][0] = 1
    # print(dict)
    # f2.write("The label "+"'"+str(l1[1])+"'"+" being used in line "+str(instructions.index(i)+1)+" has not been defined")
    # -----------------------------------------------
    # Checking for missing hlt instruction
    hltit = False
    for qwe in instructions:
        if qwe == "hlt":
            hltit = True
    # -----------------------------------------------
# Checking the misuse of labels as variables or vice versa
for oppy in vari:
    if oppy in label:
        correct = False
        f2.write("You cannot use the same name " + str(oppy) + " for both variable and label \n")
if hltit:
    if instructions[len(instructions) - 1] != "hlt":
        f2.write("Please make hlt as your last instruction \n")
else:
    f2.write("hlt statement missing...Please add a last hlt statement \n")
for q in liney:
    f2.write("The variable declared at line no." + str(q) + "should be declared in the beginning \n")
for i in dict:
    if dict[i][0] == 0:
        correct = False
        f2.write("The label " + "'" + str(i) + "'" + " being used in line " + str(
            dict[i][1]) + " has not been defined" + "\n")
f2.close()
f2 = open("opcode.txt","r")
if(correct):
    for linys in f2:
        l2 = linys.split(" ")
        if l2[0]=="var":
            mem_addr.update({l2[1]:"0000000000000000"})
        if l2[0]=="add":
            add(l2[1][:2], l2[2][:2], l2[3][:2])
        if l2[0]=="mul":
            mul(l2[1][:2],l2[2][:2],l2[3][:2])
        if l2[0]=="mov" and l2[2][0]=="$":
            inti = int(l2[2][1:])
            mov_imm(l2[1][:2],inti)
        if l2[0]=="mov" and l2[2][0]!="$":
            MovReg(l2[1][:2],l2[2][:2])
        if l2[0]=="div":
            div(l2[1][:2] , l2[2][:2])
        if l2[0]=="rs" and l2[2][0]!="$":
            RightShift(l2[1][:2] , l2[2][:2])
        if l2[0]=="ls" and l2[2][0]!="$":
            LeftShift(l2[1][:2] , l2[2][:2])
        if l2[0]=="xor":
            xor(l2[1][:2] , l2[2][:2] , l2[3][:2])
        if l2[0]=="or":
            Or(l2[1][:2] , l2[2][:2] , l2[3][:2])
        if l2[0]=="and":
            And(l2[1][:2] , l2[2][:2] , l2[3][:2])
        if l2[0]=="not":
            Invert(l2[1][:2], l2[2][:2])
        if l2[0]=="hlt":
            halt                             
fz = open("binary_file.txt","w")
for zx in binary_code:
    fz.write(zx+"\n")


