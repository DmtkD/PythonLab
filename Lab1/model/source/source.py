from abc import ABC


class Source(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f'The name of source is {self._name}.'
