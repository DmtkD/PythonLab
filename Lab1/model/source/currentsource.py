from model.source.source import Source


class CurrentSource(Source):
    def __init__(self, name: str, current: float) -> None:
        super().__init__(name)
        self.current = current

    def __str__(self) -> str:
        return f'{super().__str__()} The constant current is {self.current}'
