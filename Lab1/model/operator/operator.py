class Operator:
    def __init__(self, name: str, number_of_input: int) -> None:
        self.name = name
        self.number_of_input = number_of_input

    def __str__(self) -> str:
        return f'Name: {self.name}, Number of input: number_of_input {self.number_of_input}'
