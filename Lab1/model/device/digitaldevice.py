from model.device.electricaldevice import ElectricalDevice


class DigitalDevice(ElectricalDevice):
    def __init__(self, name: str, current: int, volt: int, time: float):
        super().__init__(name, current, volt)
        self.time = time

    def __str__(self) -> str:
        return f'{super().__str__()} with {self.time} sec'
