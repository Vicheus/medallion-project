from typing import Literal, Optional

from pydantic import field_validator, Field
from pyspark.sql import Column
from pyspark.sql.functions import when, create_map, lit, coalesce, regexp_replace, array

from parsetron.engine.registry.base import (
    BaseValue,
    ActionType,
    ActionLitType,
    BaseCol,
    ColLiteral,
)
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve


class SingleCaseFn(BaseAction, BaseValue):
    fn: Literal["case"] = "case"
    condition: ActionType

    def apply(self) -> Column:
        return when(resolve(self.condition), resolve(self.value))


class CasesFn(BaseAction):
    fn: Literal["when"]
    cases: list[SingleCaseFn] = Field(min_length=1)
    otherwise: Optional[ActionLitType] = None

    def apply(self) -> Column:
        expr = self.cases[0].apply()
        if len(self.cases) > 1:
            for case in self.cases[1:]:
                expr = expr.when(resolve(case.condition), resolve(case.value))
        if self.otherwise:
            expr = expr.otherwise(resolve(self.otherwise))
        return expr

    @field_validator("cases", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class IsNotNullAndNotEqualValueFn(BaseAction, BaseCol, BaseValue):
    fn: Literal["isNotNull_ne"]
    value: ActionLitType = ColLiteral(lit="")

    def apply(self) -> Column:
        column = resolve(self.column)
        return column.isNotNull() & (column != resolve(self.value))


class TranslateMapFn(BaseAction, BaseCol):
    fn: Literal["translate_map"]
    values: dict[str, str]
    otherwise: ActionType = None

    def apply(self) -> Column:
        values = create_map([lit(x) for x in sum(self.values.items(), ())])
        if self.otherwise:
            return coalesce(values[resolve(self.column)], resolve(self.otherwise))
        return values[resolve(self.column)]


class EmptyArrayFn(BaseAction):
    fn: Literal["empty_array"]

    def apply(self) -> Column:
        return array()


class RegexpReplaceAllFn(BaseAction, BaseCol):
    fn: Literal["regexp_replace_all"]
    values: dict[str, str]

    def apply(self) -> Column:
        column = resolve(self.column)
        for k, v in self.values.items():
            column = regexp_replace(column, lit(k), lit(v))
        return column
