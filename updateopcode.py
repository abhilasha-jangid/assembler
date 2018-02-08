import os
opcode = {}

with open("opcode.txt") as handle:
    for line in handle:
        line = line.split()
        opcode[line[0]] = (line[1],line[2])


os.remove("opcode.txt")

def error(msg):
    print(msg)
    exit()



print ("MENU")
print ("1.ADD")
print ("2.UPDATE")
print ("3.SEARCH")
print ("4.DELETE")


n = int(input())


if(n==1):

    str = input("input the operant add\n")
    if(str in opcode.keys()):
        error("already exist")
    else:
        addr = input("enter address of operant\n")
        for key in opcode.keys():
            if(addr == opcode[key][0]):
                error("adress alredy in use")
        p = input("enter no. of operant\n")

        opcode[str] = (addr,p)


elif(n==2):

    str = input("input the operanter\n")
    if(str in opcode.keys()):
        addr = input("enter the update adress\n")
        for key in opcode.keys():
            if(addr == opcode[key][0] and str != opcode[key]):
                error("address already use by other operant")
        p = input("enter no of operant\n")
        opcode[str] = (addr,p)
    else:
        error("no string found")



elif( n == 3):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        print ("String exist")
    else:
        print ("String does not exist")

elif (n == 4):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        del opcode[str]
    else:
        print ("String does not exist")
        
with open("opcode.txt", 'a')as handle:
    for key in opcode.keys():
        handle.write(key+' '+opcode[key][0]+' '+opcode[key][1]+'\n')
