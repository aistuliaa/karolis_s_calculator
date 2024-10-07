class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, other_number: float) -> float:
        return self.number + other_number

    def sub(self) -> float:
        ...

    def div(self) -> float:
        ...

    def mul(self) -> float:
        ...

    def calculate(self) -> float:
        ...
 