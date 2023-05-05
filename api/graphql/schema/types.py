from __future__ import annotations

from typing import Optional

import strawberry
from strawberry.lazy_type import LazyType

from api import CAH
from api.graphql.models import *
from api.graphql.schema.inputs import *

packs = [Pack.parse_obj(p) for p in CAH]


@strawberry.experimental.pydantic.type(
    model=Pack,
    description="A pack of cards.",
)
class PackType:
    name: strawberry.auto
    id: strawberry.auto
    white: list[LazyType["WhiteCardType", __name__]]
    black: list[LazyType["BlackCardType", __name__]]

    @strawberry.field(description="The pack's black cards.")
    def black(self, where: Optional[BlackCardInput] = None) -> list[BlackCardType]:
        return [
            c
            for c in self.black
            if where is None
            or (where.text is None or where.text in c.text)
            and (where.pick is None or c.pick == where.pick)
        ]

    @strawberry.field(description="The pack's white cards.")
    def white(self, where: Optional[WhiteCardInput] = None) -> list[WhiteCardType]:
        return [
            c
            for c in self.white
            if where is None
            or (where.text is None or where.text.casefold() in c.text.casefold())
        ]


@strawberry.experimental.pydantic.type(
    model=BlackCard,
    all_fields=True,
    description="A black card.",
)
class BlackCardType:
    pass


@strawberry.experimental.pydantic.type(
    model=WhiteCard, all_fields=True, description="A white card."
)
class WhiteCardType:
    pass


@strawberry.type
class Query:
    @strawberry.field(description="A list of packs.")
    def packs(self, where: Optional[PackInput] = None) -> list[PackType]:
        return [
            p
            for p in packs
            if where is None
            or (where.name is None or p.name == where.name)
            and (where.id is None or p.id == where.id)
        ]


schema = strawberry.Schema(Query)
