from pydantic import BaseModel

class Calculation(BaseModel):
    firstNumber: str
    secondNumber: str
    operator: str