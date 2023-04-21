# co project
# Vaibhav Gupta
# Vaibhav Sehara
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
inst = []
reg = []
for j in opcode:
    inst.append(j)
reg_code =  {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110',
            'FLAGS': '111'}
for j in reg_code:
    reg.append(j)
f = open("opcode.txt","r")
f2 = open("error_file.txt","w")
f3 = open("binary_file.txt","w")
#creating a list to add each line of assembly instruction as an element of this list
instructions = []
for line in f:
    l = line.strip()
    instructions.append(l)
#Now beggining the check if the given assembly code is correct or not:
for i in instructions:
    l1=str(i).split(" ")
    # Checking part a: Typos in instruction name or register name
    #checking for the initial instruction
    if l1[0] not in inst and l1[0]!="var":
            isthere = True
            f2.write("There is a typing error in the instruction name in line number "+str(instructions.index(i)+1)+"\n")
    #now checking the typo in register name
    for m in l1:
        if m[0]=="R":
            if m not in reg:
                f2.write("There is a typing error in the register name in line number " + str(
                    instructions.index(i) + 1) + "\n")






