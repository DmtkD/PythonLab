from model.source.source import Source


class VoltageSource(Source):
    def __init__(self, name: str, internal_resistance: int, voltage: int) -> None:
        super().__init__(name)
        self.__internal_resistance = internal_resistance
        self.__voltage = voltage

    def __str__(self) -> str:
        return f'{super().__str__()} Voltage Source have constant voltage ({self.__voltage}) with resistance {self.__internal_resistance} Ohm'
