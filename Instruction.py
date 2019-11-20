register_dic = {
    "R0": "0000",
    "R1": "0001",
    "R2": "0010",
    "R3": "0011",
    "R4": "0100",
    "R5": "0101",
    "R6": "0110",
    "R7": "0111",
    "R8": "1000",
    "R9": "1001",
    "RA": "1010",
    "RB": "1011",
    "RC": "1100",
    "RD": "1101",
    "RE": "1110",
    "RF": "1111",
}

register_hex_dic = {
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "RA": "a",
    "RB": "b",
    "RC": "c",
    "RD": "d",
    "RE": "e",
    "RF": "f",
}


def add_args(args):
    arg_str = register_hex_dic[args[0]]
    arg_str += register_hex_dic[args[1]]
    arg_str += register_hex_dic[args[2]]
    arg_str += "0"
    return arg_str


def addi_args(args):
    arg_str = str(register_hex_dic[args[0]])
    arg_str += register_hex_dic[args[1]]
    hex_str = hex(int(args[2]))[2:]  # str(hex(args[2])[2:])
    if len(hex_str) == 1:
        arg_str += '0'
        arg_str += hex_str
    elif len(hex_str) == 2:
        arg_str += hex_str
    else:
        arg_str += '00'
    return arg_str


def jump_offset(offset):
    if len(offset) == 1:
        offset = "000" + offset

    elif len(offset) == 2:
        offset = "00" + offset

    elif len(offset) == 3:
        offset = "0" + offset
    return offset


def ld_offset(offset):
    if len(offset) == 1:
        offset = "00" + offset

    elif len(offset) == 2:
        offset = "0" + offset

    return offset


def branch_offset(offset):
    if len(offset) == 1:
        offset = "0" + offset
    return offset


class Instruction:
    opcode = ""
    args = []
    hex = ""

    def __init__(self, opcode, args):
        self.opcode = opcode
        self.args = args
        self.convert_line()

    def convert_line(self):
        hex_str = ""
        opcode = self.opcode

        if opcode == "0" or opcode == "1" or opcode == "2" or opcode == "3":
            hex_str += opcode
            hex_str += add_args(self.args)

        elif opcode == "4" or opcode == "5" or opcode == "6" or opcode == "7" or opcode == "b" or opcode == "c" or opcode == "d" or opcode == "e" or opcode == "f":
            hex_str += opcode
            hex_str += addi_args(self.args)

        elif opcode == "8":
            hex_str += opcode
            offset = str(hex(int(self.args[0]))[2:])
            hex_str += jump_offset(offset)

        elif opcode == "9" or opcode == "a":
            hex_str += opcode
            hex_str += register_hex_dic[self.args[0]]
            offset = str(hex(int(self.args[1]))[2:])
            hex_str += ld_offset(offset)

        self.hex = hex_str
