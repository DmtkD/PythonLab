from model.device.electricaldevice import ElectricalDevice


class OperationalAmplifier(ElectricalDevice):
    def __init__(self, name: str, current: int, volt: int, number_of_inputs: int):
        super().__init__(name, current, volt)
        self.__number_of_input = number_of_inputs

    def __str__(self) -> str:
        return f"{super().__str__()} And we have only {self.__number_of_input} inputs"
