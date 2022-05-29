from model.device.electricaldevice import ElectricalDevice


class PulsedDevice(ElectricalDevice):
    def __init__(self, name: str, current: int, volt: int, pulses_in_sec: int) -> None:
        super().__init__(name, current, volt)
        self.__pulses_in_sec = pulses_in_sec

    def __str__(self) -> str:
        return f'{super().__str__()} which have {self.__pulses_in_sec} in second'
