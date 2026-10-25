from functools import singledispatch

from pyspark.sql import Column
from pyspark.sql.functions import col, lit

from parsetron.engine.registry.base import ColLiteral
from parsetron.engine.registry.functions.base import BaseAction


@singledispatch
def resolve(config: BaseAction) -> Column:
    return config.apply()


@resolve.register
def _(config: None) -> Column:
    return lit(config)


@resolve.register(ColLiteral)
def _(config: ColLiteral) -> Column:
    return lit(config.lit)


@resolve.register(str)
def _(config: str) -> Column:
    return col(config)


@singledispatch
def resolve_expr(config: str) -> str:
    return config


@resolve_expr.register(BaseAction)
def _(config: BaseAction) -> Column:
    return resolve(config)
