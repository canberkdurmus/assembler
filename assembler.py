from Instruction import Instruction

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

opcode_hex_dict = {
    "ADD":  "0",
    "AND":  "1",
    "OR":   "2",
    "XOR":  "3",
    "ADDI": "4",
    "ANDI": "5",
    "ORI":  "6",
    "XORI": "7",
    "JUMP": "8",
    "LD":   "9",
    "ST":   "a",
    "BEQ":  "b",
    "BLT":  "c",
    "BGT":  "d",
    "BLE":  "e",
    "BGE":  "f",
}

f = open('code.txt', "r")
lines = f.readlines()
f.close()

instruction_arr = []
i = 0

for line in lines:
    line_arr = line.split()
    opcode = opcode_hex_dict[line_arr[0]]
    args = line_arr[1].split(',')
    instruction_arr.append(Instruction(opcode, args))
    print(instruction_arr[i].hex)
    i += 1

