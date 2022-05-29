from abc import ABC


class ElectricalDevice(ABC):
    def __init__(self, name: str, current: int, volt: int) -> None:
        self._name = name
        self._current = current
        self._volt = volt

    def __str__(self) -> str:
        return f'Name: {self._name}, that {self._current} in Amper'
