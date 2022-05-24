from model.operator.operator import Operator


class BinaryAdder(Operator):
    def __init__(self, name: str, number_of_input: int, voltage: int):
        super().__init__(name, number_of_input)
        self.voltage = voltage

    def __str__(self):
        return f'{super().__str__()}, Voltage: {self.voltage} Volt'
