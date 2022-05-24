from model.operator.operator import Operator


class BinaryDecimalDecoder(Operator):
    def __init__(self, name: str, number_of_input: int, current: int):
        super().__init__(name, number_of_input)
        self.current = current

    def __str__(self) -> str:
        return f"{super().__str__()}, Current: {self.current} Amp"
