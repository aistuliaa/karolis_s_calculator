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

def mul(self, other_number: float) -> float:
        return self.number * other_number

def calculate(self, other_number: float) -> float:
    if self.symbol == '+':
        return self.add(other_number)
    elif self.symbol == '-':
        return self.sub(other_number)
    elif self.symbol == '*':
        return self.mul(other_number)
    elif self.symbol == '/':
        return self.div(other_number)
    else:
        return None
        