from abc import ABC


class Operator (ABC):
    def __init__(self, name: str, number_of_input: int) -> None:
        self._name = name
        self._number_of_input = number_of_input

    def __str__(self) -> str:
        return f'Name: {self._name}, Number of input: number_of_input {self._number_of_input}'
