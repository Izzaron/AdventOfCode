import itertools

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day14input.txt")

program = [ line.strip() for line in f]

def applyMask1(number,mask):
    
    bit36number = "{:036b}".format(number)
    
    maskedNumber = [n if m=='X' else m for n,m in zip(bit36number,mask)]

    return int("".join(maskedNumber),2)

def writeToMemory1(number,adress,mask,memory):
    memory[adress] = applyMask1(number,mask)

def applyMask2(number,mask):
    
    bit36number = "{:036b}".format(number)

    maskedNumber = [n if m=='0' else m for n,m in zip(bit36number,mask)]

    return maskedNumber #list of chars

def writeToMemory2(number,adress,mask,memory):
    
    maskedAdress = applyMask2(adress,mask)

    floatingBitIndecies = [i for i, x in enumerate(maskedAdress) if x == 'X']

    for combination in itertools.product("01",repeat=len(floatingBitIndecies)):
        
        for floatingbitIndex,bit in zip(floatingBitIndecies,combination):
            maskedAdress[floatingbitIndex] = bit

        floatingAdress = int("".join(maskedAdress),2)
        memory[floatingAdress] = number

memory = dict()
globalMask = ""

for line in program:
    instruction,value = [c.strip() for c in line.split('=')]

    if line[:3] == "mem":
        number = int(value)
        adress = int(instruction.replace("mem",'').replace('[','').replace(']',''))
        # writeToMemory1(number,adress,globalMask,memory) #part 1
        writeToMemory2(number,adress,globalMask,memory) #part 2
    elif line[:3] == "mas":
        globalMask = value
    else:
        print("Unrecognized command:",line)
        break

print(sum([val for val in memory.values()]))