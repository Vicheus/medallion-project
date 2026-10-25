from typing import Literal, Callable

from pydantic import field_validator, Field, BaseModel
from pyspark.sql import Column
from pyspark.sql.functions import lit, when

from parsetron.engine.registry.base import ActionLitType, ColLiteral
from parsetron.engine.registry.base import BaseCols, BaseCol, BaseValue
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve


class NullCheck(BaseModel):
    isNullCheck: bool = True


class BoolFn(BaseCol, BaseValue, NullCheck):
    def execute(self, evaluate: Callable[[Column, Column], Column]) -> Column:
        if self.isNullCheck:
            column = resolve(self.column)
            value = resolve(self.value)
            return when(
                column.isNotNull() & value.isNotNull(), evaluate(column, value)
            ).otherwise(lit(False))
        return evaluate(resolve(self.column), resolve(self.value))


class AndFn(BaseAction, BaseCols):
    fn: Literal["and"]

    def apply(self) -> Column:
        exps = [(resolve(column)) for column in self.columns]
        result = exps[0]
        for expr in exps[1:]:
            result = result & expr
        return result


class OrFn(BaseAction, BaseCols):
    fn: Literal["or"]

    def apply(self) -> Column:
        exps = [(resolve(column)) for column in self.columns]
        result = exps[0]
        for expr in exps[1:]:
            result = result | expr
        return result


class NegationFn(BaseAction, BaseCol):
    fn: Literal["not"]

    def apply(self) -> Column:
        return ~resolve(self.column)


class EqOperatorFn(BaseAction, BaseCol, BaseValue):
    fn: Literal["eq"]

    def apply(self) -> Column:
        return resolve(self.column).eqNullSafe(resolve(self.value))


class NeOperatorFn(BaseAction, BaseCol, BaseValue):
    fn: Literal["ne"]

    def apply(self) -> Column:
        return ~(resolve(self.column).eqNullSafe(resolve(self.value)))


class GtOperatorFn(BaseAction, BoolFn):
    fn: Literal["gt"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c > v)


class GteOperatorFn(BaseAction, BoolFn):
    fn: Literal["gte"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c >= v)


class LtOperatorFn(BaseAction, BoolFn):
    fn: Literal["lt"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c < v)


class LteOperatorFn(BaseAction, BoolFn):
    fn: Literal["lte"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c <= v)


class BetweenFn(BaseAction, BaseCol, NullCheck):
    fn: Literal["between"]
    lower: ActionLitType
    upper: ActionLitType

    def apply(self) -> Column:
        if self.isNullCheck:
            column = resolve(self.column)
            return when(column.isNull(), lit(False)).otherwise(
                column.between(resolve(self.lower), resolve(self.upper))
            )
        return resolve(self.column).between(resolve(self.lower), resolve(self.upper))


class ContainsFn(BaseAction, BoolFn):
    fn: Literal["contains"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c.contains(v))


class EndswithFn(BaseAction, BoolFn):
    fn: Literal["endswith"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c.endswith(v))


class StartswithFn(BaseAction, BoolFn):
    fn: Literal["startswith"]

    def apply(self) -> Column:
        return self.execute(lambda c, v: c.startswith(v))


class IsNotNullFn(BaseAction, BaseCol):
    fn: Literal["isNotNull"]

    def apply(self) -> Column:
        return resolve(self.column).isNotNull()


class IsNullFn(BaseAction, BaseCol):
    fn: Literal["isNull"]

    def apply(self) -> Column:
        return resolve(self.column).isNull()


class IsinFn(BaseAction, BaseCol, NullCheck):
    fn: Literal["isin"]
    values: list[ActionLitType] = Field(min_length=1)

    def apply(self) -> Column:
        if self.isNullCheck:
            column = resolve(self.column)
            values = (resolve(value) for value in self.values)
            return when(column.isNull(), lit(False)).otherwise(column.isin(*values))
        values = (resolve(value) for value in self.values)
        return resolve(self.column).isin(*values)

    @field_validator("values", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class LikeFn(BaseAction, BaseCol, NullCheck):
    fn: Literal["like"]
    value: ColLiteral

    def apply(self) -> Column:
        if self.isNullCheck:
            column = resolve(self.column)
            return when(column.isNull(), lit(False)).otherwise(
                column.like(self.value.lit)
            )
        return resolve(self.column).like(self.value.lit)


class RLikeFn(BaseAction, BaseCol, NullCheck):
    fn: Literal["rlike"]
    value: ColLiteral

    def apply(self) -> Column:
        if self.isNullCheck:
            column = resolve(self.column)
            return when(column.isNull(), lit(False)).otherwise(
                column.rlike(self.value.lit)
            )
        return resolve(self.column).rlike(self.value.lit)
