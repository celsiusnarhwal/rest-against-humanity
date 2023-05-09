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
    white: list[LazyType["WhiteCardType", __name__]] = strawberry.field(
        description="The pack's white cards."
    )
    black: list[LazyType["BlackCardType", __name__]] = strawberry.field(
        description="The pack's black cards."
    )

    @strawberry.field
    def black(self, where: Optional[BlackCardInput] = None) -> list[BlackCardType]:
        return [c for c in self.black if (where or BlackCardInput()).matches(c)]

    @strawberry.field
    def white(self, where: Optional[WhiteCardInput] = None) -> list[WhiteCardType]:
        where = where or WhiteCardInput()
        return [c for c in self.white if (where or WhiteCardInput()).matches(c)]


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
        return [p for p in packs if (where or PackInput()).matches(p)]


schema = strawberry.Schema(Query)
