# co project 
# Vaibhav Gupta
# Vaibhav Sehara
opcode = {"add": ("00000", "A"), "sub": ("00001", "A"), "mov": (("00010", "B"), ("00011", "C"))
    , "ld": ("00100", "D"), "st": ("00101", "D"), "mul": ("00110", "A"), "div": ("00111", "C"),
          "rs": ("01000", "B"), "ls": ("01001", "B"), "xor": ("01010", "A"), "or": ("01011", "A"),
          "and": ("01100", "A"),
          "not": ("01101", "C"), "cmp": ("01110", "C"), "jmp": ("01111", "E"), "jlt": ("11100", "E"),
          "jgt": ("11101", 'E'), "je": ("11111", 'E'),
          "hlt": ("11010", "F")}
reg_code =  {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110',
            'FLAGS': '111'}


# define the ISA function
# just adding the function name for now

def add(x, y, z):
    
    #Performs reg1 =reg2 + reg3.If the computation overflows, then the overflow flag is set and 0 is written in reg1
    #get binary values of functions

def sub(x, y, z):
    
    # Performs reg1 = reg2 + reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1
    
def mul(x, y, z):
    
    # Performs reg1 = reg2 x reg3. If the computation overflows, then the overflow flag is set and 0 is written in reg1
    
def div(x, y, z):
    
    # Performs reg3/reg4. Stores the quotient in R0 and the remainder in R1. 
    # If reg4 is 0 then overflow flag is set and content of R0 and R1 are set to 0      

def xor(x, y, z):
    
    # Performs bitwise XOR of reg2 and reg3. Stores the result in reg1.    