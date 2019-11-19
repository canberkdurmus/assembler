opcode_dict = {
    "ADD":  "0000",
    "AND":  "0001",
    "OR":   "0010",
    "XOR":  "0011",
    "ADDI": "0100",
    "ANDI": "0101",
    "ORI":  "0110",
    "XORI": "0111",
    "JUMP": "1000",
    "LD":   "1001",
    "ST":   "1010",
    "BEQ":  "1011",
    "BLT":  "1100",
    "BGT":  "1101",
    "BLE":  "1110",
    "BGE":  "1111",
}

f = open('code.txt', "r")
lines = f.readlines()
f.close()

for line in lines:
    line_arr = line.split()
    opcode = opcode_dict[line_arr[0]]
    args = line_arr[1].split(',')
    print(opcode)
    print(args)

