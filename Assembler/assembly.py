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
ocv = ["ld","st"]
def variable_index(line):
    ind = 0
    if line[0] in ocv:
        if line[0]=="ld" or line[0]=="st":
            ind = 2
    return ind
inst = []
reg = []
label = []
for j in opcode:
    inst.append(j)
reg_code =  {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110',
            'FLAGS': '111'}
for j in reg_code:
    reg.append(j)
f = open("opcode.txt","r")
f3 = open("binary_file.txt","w")
vari = []
for lines in f:
    l2 = lines.split()
    if l2[0]=="var":
        vari.append(l2[1])
f2 = open("error_file.txt","w")
f.close()
#creating a list to add each line of assembly instruction as an element of this list
f = open("opcode.txt","r")
instructions = []
for line in f:
    l = line.strip()
    instructions.append(l)
dict = {}
#-----------------------------------------------
correct = True
#Now beggining the check if the given assembly code is correct or not:
for i in instructions:
    l1=str(i).split(" ")
    s = ""
    for o in range(len(l1)):
        if l1[0][len(l1[0])-1] == ":":
            for k in range(0, len(l1[0])-1):
                s += l1[0][k]
            label.append(s)
    print(label)
    # -----------------------------------------------

    # Checking part a: Typos in instruction name or register name
    #checking for the initial instruction
    if l1[0] not in inst and l1[0]!="var" and l1[0][len(l1[0])-1]!=":":
        correct = False
        f2.write("There is a typing error in the instruction name in line number "+str(instructions.index(i)+1)+"\n")

    # -----------------------------------------------

    #now checking the typo in register name
    for m in range(len(l1)):
        if l1[m][0]=="R" and l1[0]!="var" and m not in vari:
            if l1[m] not in reg:
                correct = False
                f2.write("There is a typing error in the register name in line number " + str(
                    instructions.index(i) + 1) + "\n")

    # -----------------------------------------------

    #now checking any use of undefined variable
    if l1[0] in ocv:
        if l1[variable_index(l1)] not in vari:
            correct = False
            f2.write("The variable "+l1[variable_index(l1)] + " used in line " +str(instructions.index(i)+1) + " is undefined ")

    # -----------------------------------------------

    #checking that all the variables are declared at the starting of the assembly code

    # -----------------------------------------------

    #now checking any undefined labels in the code
    po = ["jmp","jlt","jgt","je"]
    if l1[0] in po:
        dict.update({l1[1]:[0,instructions.index(i)+1]})
        print(dict)
    for j in dict :
        if j in label:
            dict[j][0]=1
    # print(dict)
            # f2.write("The label "+"'"+str(l1[1])+"'"+" being used in line "+str(instructions.index(i)+1)+" has not been defined")
for i in dict:
    if dict[i][0]==0:
        f2.write("The label " + "'" + str(i) + "'" + " being used in line " + str(dict[i][1])+ " has not been defined")







