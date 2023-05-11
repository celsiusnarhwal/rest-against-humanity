from __future__ import annotations

from typing import Optional

import strawberry
from pydantic import parse_obj_as
from strawberry.lazy_type import LazyType

from api import CAH
from api.graphql.models import *
from api.graphql.schema.inputs import *


@strawberry.experimental.pydantic.type(
    name="Pack",
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
    def black(self, where: Optional[BlackCardFilter] = None) -> list[BlackCardType]:
        return [c for c in self.black if (where or BlackCardFilter()).matches(c)]

    @strawberry.field
    def white(self, where: Optional[WhiteCardFilter] = None) -> list[WhiteCardType]:
        where = where or WhiteCardFilter()
        return [c for c in self.white if (where or WhiteCardFilter()).matches(c)]


@strawberry.experimental.pydantic.type(
    name="BlackCard",
    model=BlackCard,
    all_fields=True,
    description="A black card.",
)
class BlackCardType:
    pass


@strawberry.experimental.pydantic.type(
    name="WhiteCard", model=WhiteCard, all_fields=True, description="A white card."
)
class WhiteCardType:
    pass


@strawberry.type
class Query:
    @strawberry.field(description="A list of packs.")
    def packs(self, where: Optional[PackFilter] = None) -> list[PackType]:
        return [
            p
            for p in parse_obj_as(list[Pack], CAH)
            if (where or PackFilter()).matches(p)
        ]


schema = strawberry.Schema(Query)
