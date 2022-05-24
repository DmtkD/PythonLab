class ElectricalDevice:
    def __init__(self, name: str, current: int, volt: int) -> None:
        self.name = name
        self.current = current
        self.volt = volt

    def __str__(self) -> str:
        return f'Name: {self.name}, that {self.current} in Amper'
