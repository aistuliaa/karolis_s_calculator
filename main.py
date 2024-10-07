class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, other_number: float) -> float:
        return self.number + other_number

    def sub(self, other_number: float) -> float:
        return self.number - other_number
    
    def div(self, other_number: float) -> float:
        try:
            return self.number / other_number
        except ZeroDivisionError:
            return None 

    def mul(self) -> float:
        ...

    def calculate(self) -> float:
        ...
 