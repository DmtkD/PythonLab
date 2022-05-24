from model.source.source import Source


class VoltageSource(Source):
    def __init__(self, name: str, internal_resistance: int, voltage: int) -> None:
        super().__init__(name)
        self.internal_resistance = internal_resistance
        self.voltage = voltage

    def __str__(self) -> str:
        return f'{super().__str__()} Voltage Source have constant voltage ({self.voltage}) with resistance {self.internal_resistance} Ohm'
