opcode= {}
pseudo= []

symbol = {}
icf = []

#fetching data from opcode file

with open("opcode.txt") as handle:
    for line in handle:
        line = line.split()
        opcode[line[0]]=(line[1],line[2])

        
# feching data from pseudo file
with open("pseudo.txt") as handle:
    for line in handle:
        line = line.split()
        pseudo.append(line[0])

        

# declare the location counter
location_counter = 1000


#print erroe msg
def error(msg):
    print (msg)
    exit()


# update location counter if operant is in pseudo file
def pseudoLine(line,location_counter):
    if(line[0] == 'BYTE'):
        if(len(line) == 3):
            icf.append(line[2])
            symbol[line[1]] = location_counter
        else:
            error('error invalid length of byte')
    elif(line[0] == 'RESB'):
        if(len(line) == 2):
            icf.append(0)
            symbol[line[1]] = location_counter
        else:
            error('error invalid length of RESB')
    return 1



# if operand in opcode file
def opcodeLine(line):
    len_operant = len(line)-1
    if(int(opcode[line[0]][1]) != len_operant):
        error('error in opcode length!!')
    else:
        icf.append(opcode[line[0]][0])
        for i in range(1,len_operant+1):
            icf.append(line[i])
            if not line[i].startswith('R'):
                if line[i] not in symbol.keys():
                    symbol[line[i]]= -1
        return(len(line))


#labals checking in file
def label(line,location_counter):
    if(line[0] in symbol.keys()):
        error('already exist in table')
    else:
        symbol[line[0]] = location_counter
        list.pop(0)
        return process(line,location_counter)
        
            
 

# search for the symbol in file
def process(line,location_counter):
    if(line[0] in pseudo):
        return pseudoLine(line,location_counter)
    elif( line[0] in opcode.keys()):
        return opcodeLine (line)
    else:
        if(line[0].endswith(':')):
            return labal(line,locationcounter)
        else:
            error(line[0])
        

# feching data from input file
with open("input.txt") as handle:
    start = False
    end = False
    for line in handle:
        line = line.split()
        if(start == False):
            if(line[0] == 'START'):
                start = True
                if(len(line) == 2):
                    location_counter = int(line[1])
            else:
                error('first line should be start')
        elif (end == False):
            if(line[0] == 'END'):
                end = True
            else:
                location_counter = location_counter + process(line,location_counter)
        elif (end == True):
            error('error nothing come after end')
    if(end == False):
        error('error end is missing')
            
for key in symbol.keys():
    if(int(symbol[key])== -1):
        error(key+"NOT Found")

print(symbol)
print(icf)
            
                


