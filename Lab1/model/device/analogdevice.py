from model.device.electricaldevice import ElectricalDevice


class AnalogDevice(ElectricalDevice):
    def __init__(self, name: str, current: int, volt: int, period: int) -> None:
        super().__init__(name, current, volt)
        self.period = period

    def __str__(self) -> str:
        return f'{super().__str__()} with period: {self.period}'
