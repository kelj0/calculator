from fastapi import APIRouter
import typing as tp
from app.datamodels import Calculation

from app.helpers import load_operators_from_database, do_calculation

router = APIRouter(
    prefix="/calculator",
    tags=["calculator"],
    responses={404: {"description":"Not found"}},
)

@router.post("/calculate")
async def calculate(
    calculation: Calculation
) -> tp.Dict[tp.AnyStr, tp.AnyStr]:
    """
    Return a result from doing a calculation.
    - **firstNumber**: first number in calculation
    - **secondNumber**: second number in calculation
    - **operator**: operator used for the calculation
    """
    result = do_calculation(
        calculation.firstNumber,
        calculation.secondNumber,
        calculation.operator
    )
    return {"result": str(result)}


@router.get("/operators")
async def operators() -> tp.Dict[tp.AnyStr, tp.List]:
    """
    Return a list of operators that are supported by the app
    returns `dict(str, list)`
    """
    operators = load_operators_from_database()
    return {"operators": operators}
