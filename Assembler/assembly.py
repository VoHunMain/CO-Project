# co project
# Vaibhav Gupta
# Vaibhav Sehara
import random
def check_int(x):
    hai = True
    for i in x:
        if i not in num:
            hai = False
    return hai
num = ["1","2","3","4","5","6","7","8","9"]
def gbs(n):
    # Generate a random number with n bits
    number = random.getrandbits(n)
    # Convert the number to binary
    binary_string = format(number, '0b')
    return binary_string

correct = True
# global variable FLAGS and binary_code.
registers = ["0000000000000000"] * 7  # R0 to R6
mem_addr = {}
flag = [0] * 4  # V L G E
binary_code = []
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
        f2.write("Error in line " + str(instructions.index(i) + 1) +": "+"Invalid operand "+ "\n")

    # -----------------------------------------------

    # now checking the typo in register name
    for m in range(len(l1)):
        if l1[m][0] == "R" and l1[0] != "var" and m not in vari:
            if l1[m] not in reg:
                correct = False
                f2.write("Error in line number " + str(
                    instructions.index(i) + 1) +": "+"Invalid register name"+ "\n")

    # -----------------------------------------------

    # now checking any use of undefined variable
    if l1[0] in ocv:
        if l1[variable_index(l1)] not in vari:
            correct = False
            f2.write("Error in line number "+str(instructions.index(i) + 1)+": "+"No variable name " + l1[variable_index(l1)] +"\n")

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
    # Checking the illegal use of FLAGS register
    illegal = False
    for io in range(len(instructions)):
        lz = instructions[io].split(" ")
        if len(lz)==3:
            if lz[2]=="FLAGS":
                if lz[0]!="mov" or lz[1] not in reg_code:
                    correct = False
                    illegal = True
    # -----------------------------------------------

    #now checking any undefined labels in the code
    # po = ["jmp", "jlt", "jgt", "je"]
    # if l1[0] in po:
    #     dict.update({l1[1]: [0, instructions.index(i) + 1]})
    # for j in dict:
    #     if j in label:
    #         dict[j][0] = 1
    # print(dict)
    # f2.write("The label "+"'"+str(l1[1])+"'"+" being used in line "+str(instructions.index(i)+1)+" has not been defined")
    # -----------------------------------------------
    # Checking for missing hlt instruction
    hltit = False
    for money in range(len(instructions)):
        if instructions[money]!="hlt" and money == len(instructions)-1:
            correct = False
    # -----------------------------------------------
# Checking the misuse of labels as variables or vice versa
for oppy in vari:
    if oppy in label:
        correct = False
        f2.write("You cannot use the same name " + str(oppy) + " for both variable and label \n")
hltbnl= False
hltnt = False
for ko in range(len(instructions)):
    if instructions[ko]=="hlt" and ko != len(instructions)-1:
        correct = False
        hltbnl = True
if hltbnl:
    f2.write("Please make hlt as your last instruction \n")
for ok in range(len(instructions)):
    if instructions[ok] != "hlt" and ok == len(instructions) - 1:
        correct = False
        hltnt = True
if hltnt:
    f2.write("Halt statement missing.....Please add a last halt statement")
for q in liney:
    f2.write("The variable declared at line no." + str(q) + "should be declared in the beginning \n")
for i in dict:
    if dict[i][0] == 0:
        correct = False
        f2.write("The label " + "'" + str(i) + "'" + " being used in line " + str(
            dict[i][1]) + " has not been defined" + "\n")
if illegal:
    f2.write("The FLAGS register has been illegaly used\n")
f2.close()
f2 = open("opcode.txt", "r")
f3 = open("error_file.txt","a")
# TYPE - A -START

# Opcode(5 bits)  Unused(2 bits)   reg1(3 bits)   reg2(3 bits)   reg3(3 bits)
def add(x, y, z):
    # Performs reg1 =reg2 + reg3.If the computation overflows, then the overflow flag is set and 0 is written in reg1
    # get binary values of functions
    if x not in reg_code or y not in reg_code or z not in reg_code:
        correct = False
    else:
        global flag
        adds = int(str(registers[int(y[1])]), 2) + int(str(registers[int(z[1])]), 2)
        # Check for overflow
        if int(str(registers[int(y[1])]), 2) + int(str(registers[int(z[1])]), 2) > int("1" * 16, 2):
            flag[0] = 1  # Set V flag if overflow occurs
        else:
            flag[0] = 0  # Clear V flag if no overflow occurs

    # Add values in y and z registers and store in x register
    if correct:
        registers[int(x[1])] = bin(adds)[2:].zfill(16)

    binary_code.append(opcode["add"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def sub(x, y, z):
    # Performs reg1 = reg2 + reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1
    if y not in reg_code or z not in reg_code:
        correct = False
    else:
        subs = int(str(registers[int(y[1])]), 2) - int(str(registers[int(z[1])]), 2)

        # check if subtraction will result in overflow
        if int(str(registers[int(z[1])]), 2) > int(str(registers[int(y[1])]), 2):
            flag[0] = 1
            registers[int(x[1])] = "0000000000000000"
        else:
            flag[0] = 0
            registers[int(x[1])] = bin(subs)[2:].zfill(16)

        # update register value and append binary code to list

        binary_code.append(str(opcode["sub"][0]) + "00" + str(reg_code[x]) + str(reg_code[y]) + str(reg_code[z]))


def mul(x, y, z):
    # Performs reg1 = reg2 x reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1
    # checking for overflow and setting FLAG.
    if y not in reg_code or z not in reg_code:
        correct = False
    else:
        mult = 0
        mult = int(str(registers[int(y[1])]), 2) * int(str(registers[int(z[1])]), 2)
        if mult > int("1" * 16, 2):
            flag[0] = "1"  # Set V flag if overflow occurs
            # registers[x] = "0000000000000000"  # Set reg1 to 0
        else:
            flag[0] = "0"  # Clear V flag if no overflow
            registers[int(x[1])] = bin(mult)[2:].zfill(16)

        binary_code.append(opcode["mul"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def Or(x, y, z,lines):
    # Performs bitwise OR of reg2 and reg3. Stores the result in reg1.
    if x not in reg_code or y not in reg_code or z not in reg_code:
        f3.write("Error in line number "+str(lines)+": "+"Please check the register name\n")
        correct = False
    else:
        binary_code.append(opcode["or"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def xor(x, y, z,lines):
    # Performs bitwise XOR of reg2 and reg3. Stores the result in reg1.
    if x not in reg_code or y not in reg_code or z not in reg_code:
        f3.write("Error in line number "+str(lines)+": "+"Please check the register name\n")
        correct = False
    else:
        binary_code.append(opcode["xor"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


def And(x, y, z,lines):
    ## Appending the opcode of and instruction along with the syntax supposed for the and instruction
    if x not in reg_code or y not in reg_code or z not in reg_code:
        f3.write("Error in line number "+str(lines)+": "+"Please check the register name\n")
        correct = False
    else:
        binary_code.append(opcode["and"][0] + "00" + reg_code[x] + reg_code[y] + reg_code[z])


# TYPE A - END

# - --- ---- ----- ----------- ---------------- ---------- ----------------- ---------- --------- ------------- -------- ---------- -----------------------------

# TYPE - B - START

# Opcode(5 bits)  Unused(1 bit)   reg1(3 bits)   Immediate value(7 bits)

def mov_imm(x, y):
    binary = bin(int(y))  # ---------> covert string to binary by removing the 0b.
    if x not in reg_code:
        correct = False
    if (len(binary[2:]) < 8):  ##CHECKING IF LENGTH OF binary less than 8
        extras = 7 - len(binary[2:])  ##Adding extra zeroes if required
        imm = str("0" * extras) + binary[2:]
        registers[int(x[1])] = "000000000" + str(imm)
    else:
        registers[int(x[1])] = "".zfill(16)
    binary_code.append(
        str(opcode["mov"][0][0]) + "0" + str(reg_code[x]) + str(imm))  ## mov [0][0], as we have 2 "mov" function.


def RightShift(x, y,lines):
    # Right shifts reg1 by $Imm, where $Imm is a 7 bit value.
    if  x not in reg_code:
        f3.write("Error in line number "+str(lines)+": "+"Invalid register name\n")
        correct = False
        kyaa = False
    binary = bin(int(y))  # ---------> covert string to binary by removing the 0b.
    if (len(binary[2:]) < 8) and kyaa:  ##CHECKING IF LENGTH OF binary less than 8
        extras = 7 - len(binary[2:])
        imm = str("0" * extras) + binary[2:]
        binary_code.append(opcode["rs"][0] + "0" + reg_code[x] + str(imm))
    else:
        if len(binary)>7:
            f3.write("Error in line number "+str(lines)+": "+"The immediate value should not be more than 7 bits\n")
        imm = binary[2:]

    # value = int(registers[x], 2)  # get current value in register x
    # new_value = value >> imm  # perform the right shift operation
    # registers[x] = format(new_value, '016b')  # store the new value in register x


def LeftShift(x, y,lines):
    if  x not in reg_code:
        f3.write("Error in line number "+str(lines)+": "+"Invalid register name\n")
        correct = False
        kyaa = False
    binary = bin(int(y))  # ---------> covert string to binary by removing the 0b.
    if (len(binary[2:]) < 8) and kyaa:  ##CHECKING IF LENGTH OF binary less than 8
        extras = 7 - len(binary[2:])
        imm = str("0" * extras) + binary[2:]
        binary_code.append(opcode["rs"][0] + "0" + reg_code[x] + str(imm))
    else:
        if len(binary)>7:
            f3.write("Error in line number "+str(lines)+": "+"The immediate value should not be more than 7 bits\n")
        imm = binary[2:]


##TYPE B ends

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

##TYPE C starts


def MovReg(x, y):
    if x not in reg_code or y not in reg_code :
        correct = False
    if y!="FL":
        cont1 = registers[int(y[1])]
        registers[int(x[1])] = cont1
        binary_code.append(opcode["mov"][1][0] + "00000" + reg_code[x] + reg_code[y])
    elif y== "FL":
        adds = ""
        for zx in flag:
            adds+=str(zx)
        registers[int(x[1])]= "0"*12+adds
        binary_code.append(opcode["mov"][1][0] + "00000" + reg_code[x] + "111")
# Initialize R0 and R1 to 0
# reg["R0"] = 0
# reg["R1"] = 0

def div(x, y,lines):
    # Performs reg3/reg4. Stores the quotient in R0 and the remainder in R1.
    # If reg4 is 0 then overflow flag is set and content of R0 and R1 are set to 0
    #Doubtful
    if x not in reg_code or y not in reg_code:
        f3.write("Error in line "+str(lines)+": "+"Please check the register name")
        correct = False
    else:
        binary_code.append(opcode["div"][0] + "00000" + reg_code[x] + reg_code[y])


def Invert(x, y):
    # Performs bitwise NOT of reg2. Stores the result in reg1.

    binary_code.append(opcode["not"][0] + "00000" + reg_code[x] + reg_code[y])


def Compare(x, y):
    # Compares reg1 and reg2 and sets up the FLAGS register.
    if correct:
        global flag

        val_x = int(registers[int(x[1])], 2)
        val_y = int(registers[int(y[1])], 2)

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

def load(x, y):
    # Loads data from mem_addr into reg1.
    if y in vari:
        data = mem_addr[y]
    else:
        f2.write("Error in line number " + y + " has not been defined\n")
    binary_code.append(opcode["ld"][0] + "0" + reg_code[x] + y)


def store(x, y):
    # Stores data from reg1 to mem_addr.

    if (len(y) < 8):
        extras = 7 - len(y)  ##Adding extra zeroes if required
        imm = str("0" * extras) + y
    else:
        imm = y[2:]

    binary_code.append(opcode["st"[0] + "00000" + reg_code[x] + imm])


# TYPE D ENDS HERE

# TYPE E STARTS HERE
def unconditional_jump(address):
    global correct
    # Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address.
    if str(address[:1]) not in vari:
        correct = False
        f3.write("The memory address " + address + " does not exist\n")
    else:
        binary_code.append(opcode["jmp"][0] + "0000" + str(mem_addr[str(address[:1])][0]))


def jumpifless(address):
    global correct
    # Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address.
    if str(address[:1]) not in vari:
        correct = False
        f3.write("The memory address " + address + " does not exist\n")
    else:
        binary_code.append(opcode["jlt"][0] + "0000" + str(mem_addr[str(address[:1])][0]))

def jumpifgreater(address):
    global correct
    # Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address.
    if str(address[:1]) not in vari:
        correct = False
        f3.write("The memory address " + address + " does not exist\n")
    else:
        binary_code.append(opcode["jgt"][0] + "0000" + str(mem_addr[str(address[:1])][0]))



def jumpifequal(address):
    global correct
    # Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address.
    if str(address[:1]) not in vari:
        correct = False
        f3.write("The memory address " + address + " does not exist\n")
    else:
        binary_code.append(opcode["je"][0] + "0000" +str(mem_addr[str(address[:1])][0]))



# TYPE E ENDS HERE

# TYPE F STARTS HERE
def invalid_param(line,n,func):
    f3.write("Error in line number "+line+": "+func+" must contain "+n+" parameters\n")
def halt():
    binary_code.append(opcode["hlt"][0] + "0" * 11)
naa = True
# TYPE F ENDS HERE
lines = 0
for linys in f2:
    l2 = linys.split()
    if l2[0] == "var":
        lines+=1
        k = gbs(7)
        if len(k)<7:
            extra = 7-len(k)
            k = k+"0"*extra
        mem_addr.update({l2[1][:1]: [k, "0000000000000000"]})
    if l2[0] == "add":
        lines+=1
        if len(l2)==4:
            add(l2[1][:2], l2[2][:2], l2[3][:2])
        else:
            invalid_param(str(lines),"3","add")
            correct = False
    if l2[0] == "mul":
        lines+=1
        if len(l2)==4:
            mul(l2[1][:2], l2[2][:2], l2[3][:2])
        else:
            invalid_param(str(lines),"3","mul")
            correct = False
    if l2[0] == "mov" and l2[2][0] == "$":
        lines+=1
        inti = l2[2][1:]
        for pag in inti:
            if pag not in num:
                naa =False
        if len(l2)!=3 or naa == False:
            correct = False
        else:
            mov_imm(l2[1], int(inti))
    if l2[0] == "mov" and l2[2][0] != "$":
        lines+=1
        regg = ""
        for z in range(2):
            regg+=l2[2][z]
        if len(l2)!=3 and regg not in reg_code:
            correct = False
        elif regg[0]=="F":
            MovReg(l2[1], regg)
        else:
            MovReg(l2[1],regg)
    if l2[0]=="st":
        lines+=1
        if l2[1] not in reg_code:
            f3.write("Error in line "+str(lines)+": "+"Invalid operand\n")
            correct = False
    if l2[0]=="ld":
        lines+=1
        if l2[1] not in reg_code:
            f3.write("Error in line " + str(lines) + ": " + "Invalid operand\n")
            correct = False
    if l2[0] == "div":
        lines+=1
        if len(l2)!=3:
            invalid_param(str(lines),"2","div")
            lenc = True
        if not lenc:
            div(l2[1], l2[2][::1],lines)
    if l2[0] == "rs":
        lines+=1
        if len(l2)!=3:
            invalid_param(str(lines),"2","rs")
        else:
            RightShift(l2[1], str(l2[2][1:][::1]),lines)
    if l2[0] == "ls":
        lines+=1
        if len(l2)!=3:
            invalid_param(str(lines),"2","rs")
        else:
            LeftShift(l2[1], str(l2[2][1:][::1]),lines)
    if l2[0] == "xor":
        lines+=1
        if len(l2)!=4:
            invalid_param(str(lines),"3","xor")
        else:
            xor(l2[1], l2[2], l2[3][::1],lines)
    if l2[0] == "or":
        lines+=1
        if len(l2)!=4:
            invalid_param(str(lines),"3","xor")
        else:
            Or(l2[1], l2[2], l2[3][::1],lines)
    if l2[0] == "and":
        lines+=1
        if len(l2)!=4:
            invalid_param(str(lines),"3","xor")
        else:
            And(l2[1], l2[2], l2[3][::1],lines)
    if l2[0] == "not":
        lines+=1
        if len(l2)!=3:
            invalid_param(str(lines),"2","not")
        else:
            Invert(l2[1], l2[2][:2])
    if l2[0] == "cmp":
        lines+=1
        Compare(l2[1], l2[2][:2])
    if l2[0]== "jmp":
        lines+=1
        unconditional_jump(l2[1][:2])
    if l2[0]== "jlt":
        lines+=1
        jumpifless(l2[1][:2])
    if l2[0]== "je":
        lines+=1
        jumpifequal(l2[1][:2])
    if l2[0]== "jgt":
        lines+=1
        jumpifgreater(l2[1][:2])
    if l2[0] == "hlt":
        lines+=1
        halt()
if correct:
    fz = open("binary_file.txt", "w")
    for zx in binary_code:
        fz.write(zx + "\n")
