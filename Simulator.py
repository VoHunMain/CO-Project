import numpy as np
import linecache
from FinalAssembler import label as l
from FinalAssembler import vari
from FinalAssembler import total_lines
from FinalAssembler import correct
total_lines += len(vari)
Llist = []
for i in l:
    start_index = l[i][0]
    Llist.append(start_index)
    for k in range(l[i][1]-1):
        start_index+=1
        Llist.append(start_index)
binlist = []
mem_addr = {}
pc =1
pc_stack = []
def bti(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
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
memory = ["0000000000000000"]*128
#TypeA instrucitons
flag = [0,0,0,0]
def add(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final  = bin(mem_r2+mem_r3)[2:]
    if len(str(final))>7:
        flag[0]=1
        memory[r1]="".zfill(16)
    else:
        memory[r1] = str(bin(mem_r2+mem_r3)[2:].zfill(16))
def sub(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final  = bin(mem_r2-mem_r3)[2:]
    if len(str(final))>7:
        flag[0]=1
        memory[r1]="".zfill(16)
    else:
        memory[r1] = str(bin(mem_r2-mem_r3)[2:].zfill(16))
def Mult(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final  = bin(mem_r2*mem_r3)[2:]
    if len(str(final))>7:
        flag[0]=1
        memory[r1]="".zfill(16)
    else:
        memory[r1] = str(bin(mem_r2*mem_r3)[2:].zfill(16))
def XOR(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final = bin(np.bitwise_xor(mem_r2,mem_r3))[2:]
    memory[r1] = str(final.zfill(16))
def OR(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final = bin(np.bitwise_or(mem_r2,mem_r3))[2:]
    memory[r1] = str(final.zfill(16))
def AND(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    r3 = bti(int(list[3]))
    mem_r2 = bti(int(memory[r2]))
    mem_r3 = bti(int(memory[r3]))
    final = np.bitwise_and(mem_r2,mem_r3)
    memory[r1] = str(bin(final)[2:].zfill(16))
#TypeB instructions
def mov_imm(list):
    reg = bti(int(list[1]))
    memory[reg]=str(list[2].zfill(16))
def right_shift(list):
    reg = bti(int(list[1]))
    num = bti(int(list[2]))
    mem = bti(int(memory[reg]))
    final = mem >> num
    memory[reg]=str(bin(final)[2:]).zfill(16)
def left_shift(list):
    reg = bti(int(list[1]))
    num = bti(int(list[2]))
    mem = bti(int(memory[reg]))
    final = mem << num
    memory[reg]=str(bin(final)[2:]).zfill(16)
#TypeC instructions
def mov_reg(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    mem = bti(int(memory[r2]))
    final = bin(mem)[2:].zfill(16)
    memory[r1]= str(final)
#def divide(list):
 #   return 0
def Invert(list):
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    mem = memory[r2]
    ans = ""
    for i in mem:
        if i=="0":
            ans +="1"
        if i=="1":
            ans+="0"
    memory[r1]=ans
def compare(list):
    global flag
    r1 = bti(int(list[1]))
    r2 = bti(int(list[2]))
    if(r1>r2):
        flag[2] = 1
    if(r1<r2):
        flag[1]=1
    if (r1==r2):
        flag[3]=1

#TypeD instructions
def load(list):
    addr = list[2]
    reg = bti(int(list[1]))
    data = ""
    for i in mem_addr:
        if i==addr:
            data = mem_addr[i]
            break
    memory[reg] = data
def store(list):
    r1 = bti(int(list[1]))
    f = bti(int(list[2]))
    tba = total_lines-f
    mem_addr.update({bin(tba)[2:]:memory[r1]})
#TypeE instructions
def unconditional_jump(list):
    global pc
    pc = bti(int(list[1]))
    return pc
def jlt(list):
    global flag
    global pc
    if flag[1]==1:
        pc = bti(int(list[1]))
    flag[1]=0
    return pc
def jgt(list):
    global flag
    global pc
    hai= False
    if flag[2]==1:
        hai = True
        pc = bti(int(list[1]))
    flag[2] = 0
    return [pc,hai]
def je(list):
    global flag
    global pc
    hai= False
    if flag[3]==1:
        hai = True
        pc = bti(int(list[1]))
    flag[1] = 0
    return [pc,hai]
#TypeF instructions

#-------------------------------------
A = ["00000","00001","00110","01010","01011","01100"]
B = ["00010","01000","01001"]
C = ["00011","00111","01101","01110"]
D = ["00100","00101"]
E = ["01111","11100","11101","11111"]
F = ["11010"]
def opsy(line):
    s = ""
    for i in range(0,5):
        s+=line[i]
    return s
starting=1
while starting in Llist:
    starting +=1
pc=starting
pc_stack.append(starting)
while(opsy(linecache.getline(r"Stdout.txt",pc))!="11010"):
        lines = linecache.getline(r"Stdout.txt",pc_stack[len(pc_stack)-1])
        opcode = opsy(linecache.getline(r"Stdout.txt",pc_stack[len(pc_stack)-1]))
        pc = pc_stack[len(pc_stack)-1]
        if opcode in A:
            list = TypeA(lines)
            if(opcode=="00000"):
                add(list)
            if(opcode == "00001"):
                sub(list)
            if(opcode=="00110"):
                Mult(list)
            if(opcode=="01010"):
                XOR(list)
            if(opcode=="01011"):
                OR(list)
            if(opcode=="01100"):
                AND(list)
            if pc in Llist and pc+1 in Llist:
                pc+=1
                pc_stack.pop()
                pc_stack.append(pc)
            if pc in Llist and pc+1 not in Llist:
                pc_stack.pop()
            if pc not in Llist:
                pc = pc_stack[len(pc_stack)-1]
                for k in range(pc+1,total_lines+1):
                    if k in Llist:
                        continue
                    else:
                        pc = k
                        pc_stack.pop()
                        pc_stack.append(pc)
                        break

        if opcode in B:
            list = TypeB(lines)
            if(opcode == "00010"):
                mov_imm(list)
            if(opcode=="01000"):
                right_shift(list)
            if(opcode=="01001"):
                left_shift(list)
            if pc in Llist and pc+1 in Llist:
                pc+=1
                pc_stack.pop()
                pc_stack.append(pc)
            if pc in Llist and pc+1 not in Llist:
                pc_stack.pop()
            if pc not in Llist:
                pc = pc_stack[len(pc_stack)-1]
                for k in range(pc+1,total_lines+1):
                    if k in Llist:
                        continue
                    else:
                        pc = k
                        pc_stack.pop()
                        pc_stack.append(pc)
                        break
        if opcode in C:
            list = TypeC(lines)
            if(opcode=="00011"):
                mov_reg(list)
            if(opcode=="01101"):
                Invert(list)
            if(opcode=="01110"):
                compare(list)
            if pc in Llist and pc+1 in Llist:
                pc+=1
                pc_stack.pop()
                pc_stack.append(pc)
            if pc in Llist and pc+1 not in Llist:
                pc_stack.pop()
            if pc not in Llist:
                pc = pc_stack[len(pc_stack)-1]
                for k in range(pc+1,total_lines+1):
                    if k in Llist:
                        continue
                    else:
                        pc = k
                        pc_stack.pop()
                        pc_stack.append(pc)
                        break
        if opcode in D:
            list = TypeD(lines)
            if(opcode=="00100"):
                load(list)
            if(opcode=="00101"):
                store(list)
            if pc in Llist and pc+1 in Llist:
                pc+=1
                pc_stack.pop()
                pc_stack.append(pc)
            if pc in Llist and pc+1 not in Llist:
                pc_stack.pop()
            if pc not in Llist:
                pc = pc_stack[len(pc_stack)-1]
                for k in range(pc+1,total_lines+1):
                    if k in Llist:
                        continue
                    else:
                        pc = k
                        pc_stack.pop()
                        pc_stack.append(pc)
                        break
        if opcode in E:
            list = TypeE(lines)
            if(opcode=="01111"):
                pc_stack.pop()
                pc_stack.append(unconditional_jump(list))
            if(opcode=="11100"):
                pc_stack.pop()
                pc_stack.append(jlt(list))
            if(opcode=="11101"):
                hai = False
                if pc in Llist:
                    hai = True
                le = jgt(list)
                if le[1] and hai == False:
                    pc = pc_stack[len(pc_stack)-1]
                    pc_stack.pop()
                    for k in range(pc+1,total_lines+1):
                        if k in Llist:
                            continue
                        else:
                            pc = k
                            pc_stack.append(pc)
                            break
                    pc = jgt(list)[0]
                    pc+=1
                    pc_stack.append(pc)
                elif le[1] and hai==True:
                    if pc+1 in Llist:
                        pc_stack[len(pc_stack)-1]+=1
                    else:
                        pc_stack.pop()
                    pc = jgt(list)[0]
                    pc+=1
                    pc_stack.append(pc)
                else:
                    pc = pc_stack[len(pc_stack)-1]
                    pc_stack.pop()
                    for k in range(pc+1,total_lines+1):
                        if k in Llist:
                            continue
                        else:
                            pc = k
                            pc_stack.append(pc)
                            break
            if(opcode=="11111"):
                hai = False
                if pc in Llist:
                    hai = True
                le = je(list)
                if le[1] and hai == False:
                    pc = pc_stack[len(pc_stack)-1]
                    pc_stack.pop()
                    for k in range(pc+1,total_lines+1):
                        if k in Llist:
                            continue
                        else:
                            pc = k
                            pc_stack.append(pc)
                            break
                    pc = je(list)[0]
                    pc+=1
                    pc_stack.append(pc)
                elif le[1] and hai==True:
                    if pc+1 in Llist:
                        pc_stack[len(pc_stack)-1]+=1
                    else:
                        pc_stack.pop()
                    pc = je(list)[0]
                    pc+=1
                    pc_stack.append(pc)
                else:
                    pc = pc_stack[len(pc_stack)-1]
                    pc_stack.pop()
                    for k in range(pc+1,total_lines+1):
                        if k in Llist:
                            continue
                        else:
                            pc = k
                            pc_stack.append(pc)
                            break
        # print(bin(pc-1)[2:].zfill(7) + " "+str(memory[0]) + " "+str(memory[1]) + " "+str(memory[2]) + " "+str(memory[3]) + " "+str(memory[4]) + " "+str(memory[5]) + " "+str(memory[6]) + " "+str(memory[7]))
for i in mem_addr:
    memory[7+bti(int(i))]=mem_addr[i]
for i in range(7,len(memory)):
    print(memory[i])
print(memory)
