from typing import Literal, Optional

from pydantic import Field, model_validator
from pydantic_core.core_schema import ValidationInfo
from pyspark.sql import Column
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    coalesce,
    concat,
    explode,
    greatest,
    length,
    lower,
    concat_ws,
    replace,
    regexp_replace,
    size,
    split,
    trim,
    upper,
    struct,
    from_unixtime,
    from_json,
    regexp_extract,
    regexp_extract_all,
    lpad,
    translate,
    array_join,
    initcap,
    substring,
    slice,
    when,
    try_element_at,
    array_sort,
    expr,
    array_remove,
)

from parsetron.engine.registry.base import (
    BaseCol,
    BaseCols,
    ActionLitType,
    ColLiteral,
    ActionType,
    BaseValue,
)
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve


class ArrayFn(BaseAction, BaseCols):
    fn: Literal["array"]

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return array(*values)


class ArrayCompactFn(BaseAction, BaseCol):
    fn: Literal["array_compact"]

    def apply(self) -> Column:
        return array_compact(resolve(self.column))


class ArrayDistinctFn(BaseAction, BaseCol):
    fn: Literal["array_distinct"]

    def apply(self) -> Column:
        return array_distinct(resolve(self.column))


class ArrayRemoveFn(BaseAction, BaseCol, BaseValue):
    fn: Literal["array_remove"]

    def apply(self) -> Column:
        return array_remove(resolve(self.column), resolve(self.value))


class CoalesceFn(BaseAction, BaseCols):
    fn: Literal["coalesce"]

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return coalesce(*values)


class ConcatFn(BaseAction, BaseCols):
    fn: Literal["concat"]

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return concat(*values)


class ConcatWsFn(BaseAction, BaseCols):
    fn: Literal["concat_ws"]
    sep: ColLiteral = ColLiteral(lit=" ")

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return concat_ws(self.sep.lit, *values)


class ExplodeFn(BaseAction, BaseCol):
    fn: Literal["explode"]

    def apply(self) -> Column:
        return explode(resolve(self.column))


class GreatestFn(BaseAction, BaseCols):
    fn: Literal["greatest"]

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return greatest(*values)


class LengthFn(BaseAction, BaseCol):
    fn: Literal["length"]

    def apply(self) -> Column:
        return length(resolve(self.column))


class LowerFn(BaseAction, BaseCol):
    fn: Literal["lower"]

    def apply(self) -> Column:
        return lower(resolve(self.column))


class ReplaceFn(BaseAction, BaseCol):
    fn: Literal["replace"]
    pattern: ActionLitType
    replacement: Optional[ActionLitType] = None

    def apply(self) -> Column:
        if self.replacement:
            return replace(
                resolve(self.column), resolve(self.pattern), resolve(self.replacement)
            )
        return replace(resolve(self.column), resolve(self.pattern))


class RegexpReplaceFn(BaseAction, BaseCol):
    fn: Literal["regexp_replace"]
    pattern: ActionLitType
    replacement: ActionLitType = ColLiteral(lit="")

    def apply(self) -> Column:
        return regexp_replace(
            resolve(self.column), resolve(self.pattern), resolve(self.replacement)
        )


class RegexpExtractFn(BaseAction, BaseCol):
    fn: Literal["regexp_extract"]
    pattern: ColLiteral
    index: ColLiteral

    def apply(self) -> Column:
        return regexp_extract(resolve(self.column), self.pattern.lit, self.index.lit)


class RegexpExtractAllFn(BaseAction, BaseCol):
    fn: Literal["regexp_extract_all"]
    pattern: ColLiteral
    index: Optional[ColLiteral] = None

    def apply(self) -> Column:
        if self.index:
            return regexp_extract_all(
                resolve(self.column), resolve(self.pattern), resolve(self.index)
            )
        return regexp_extract_all(resolve(self.column), resolve(self.pattern))


class SizeFn(BaseAction, BaseCol):
    fn: Literal["size"]

    def apply(self) -> Column:
        return size(resolve(self.column))


class SplitFn(BaseAction, BaseCol):
    fn: Literal["split"]
    pattern: ActionLitType
    limit: Optional[ActionLitType] = None

    def apply(self) -> Column:
        if self.limit:
            return split(
                resolve(self.column), resolve(self.pattern), resolve(self.limit)
            )
        return split(resolve(self.column), resolve(self.pattern))


class TrimFn(BaseAction, BaseCol):
    fn: Literal["trim"]
    symbols: ColLiteral = None

    def apply(self) -> Column:
        if self.symbols:
            return trim(resolve(self.column), resolve(self.symbols))
        return trim(resolve(self.column))


class UpperFn(BaseAction, BaseCol):
    fn: Literal["upper"]

    def apply(self) -> Column:
        return upper(resolve(self.column))


class StructFn(BaseAction):
    fn: Literal["struct"]
    values: dict[str, ActionLitType]

    def apply(self) -> Column:
        values = (resolve(v).alias(k) for k, v in self.values.items())
        return struct(*values)

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itms = values.get("values")
        if isinstance(itms, dict):
            itm = {}
            for key, value in itms.items():
                if isinstance(value, dict) and not (
                    len(value.keys()) == 1 and "lit" in value.keys()
                ):
                    itm[key] = BaseAction.from_dict(value, info)
                else:
                    itm[key] = value
            values["values"] = itm
        return values


class LeftPaddingFn(BaseAction, BaseCol):
    fn: Literal["lpad"]
    len: ColLiteral
    pad: ColLiteral

    def apply(self) -> Column:
        return lpad(resolve(self.column), resolve(self.len), resolve(self.pad))


class FromUnixTimeFn(BaseAction, BaseCol):
    fn: Literal["from_unixtime"]
    date_format: ColLiteral = ColLiteral(lit="yyyy-MM-dd HH:mm:ss")

    def apply(self) -> Column:
        return from_unixtime(resolve(self.column), str(self.date_format.lit))


class FromJsonFn(BaseAction, BaseCol):
    fn: Literal["from_json"]
    type: ColLiteral = Field(alias="schema")

    def apply(self) -> Column:
        return from_json(resolve(self.column), self.type.lit)


class TranslateFn(BaseAction, BaseCol):
    fn: Literal["translate"]
    matching: ColLiteral
    replace: ColLiteral

    def apply(self) -> Column:
        return translate(resolve(self.column), self.matching.lit, self.replace.lit)


class ArrayJoinFn(BaseAction, BaseCol):
    fn: Literal["array_join"]
    delimiter: ColLiteral = ColLiteral(lit=" ")

    def apply(self) -> Column:
        return array_join(resolve(self.column), self.delimiter.lit)


class CapitalizeFn(BaseAction, BaseCol):
    fn: Literal["initcap"]

    def apply(self) -> Column:
        return initcap(resolve(self.column))


class SubstringFn(BaseAction, BaseCol):
    fn: Literal["substring"]
    pos: ColLiteral = ColLiteral(lit=1)
    len: ActionType

    def apply(self) -> Column:
        return substring(resolve(self.column), self.pos.lit, resolve(self.len))


class CastFn(BaseAction, BaseCol):
    fn: Literal["cast"]
    type: ColLiteral

    def apply(self) -> Column:
        return resolve(self.column).cast(self.type.lit)


class SliceFn(BaseAction, BaseCol):
    fn: Literal["slice"]
    start: ColLiteral = ColLiteral(lit=1)
    len: ColLiteral

    def apply(self) -> Column:
        column = resolve(self.column)
        return when(column.isNotNull(), slice(column, self.start.lit, self.len.lit))


class TryElementAtFn(BaseAction, BaseCol):
    fn: Literal["try_element_at"]
    value: ColLiteral = ColLiteral(lit=1)

    def apply(self) -> Column:
        return try_element_at(resolve(self.column), resolve(self.value))


class GetFieldFn(BaseAction, BaseCol):
    fn: Literal["getField"]
    value: ColLiteral

    def apply(self) -> Column:
        return resolve(self.column)[self.value.lit]


class ArraySortFn(BaseAction, BaseCol):
    fn: Literal["array_sort"]

    def apply(self) -> Column:
        return array_sort(resolve(self.column))


class ExpressionFn(BaseAction):
    fn: Literal["expr"]
    value: ColLiteral

    def apply(self) -> Column:
        return expr(self.value.lit)
