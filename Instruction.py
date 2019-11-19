def add(opcode, args):
    print("i")



class Instruction:
    opcode = None
    args = []

    def identify_opcode(opcode, args):
        def switch_demo(opcode):
            switcher = {
                "0000": add(opcode, args),
                2: "0001",
                3: "0010",
                4: "0011",
                5: "0100",
                6: "0101",
                7: "0111",
                8: "1000",
                9: "1001",
                10: "1010",
                11: "1011",
                12: "1111"
            }
            print
            switcher.get(argument, "Invalid month")

    def __init__(self, opcode, args):
        self.opcode = opcode
        self.args = args
        self.identify_opcode(opcode, args)
