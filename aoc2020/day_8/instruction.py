class Instruction:

    def __init__(self, operator, argument):
        self.operator = operator
        self.argument = argument

    @classmethod
    def from_code_line(cls, line: str):
        operator, argument = line.split(" ", maxsplit=1)
        argument = int(argument[1:]) if argument[:1] == "+" else ((-1) * int(argument[1:]))
        return cls(operator, argument)
