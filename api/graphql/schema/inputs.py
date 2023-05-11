from typing import Optional

import strawberry

from api.graphql.models import BlackCard, Pack, WhiteCard

__all__ = ["PackFilter", "BlackCardFilter", "WhiteCardFilter"]


@strawberry.input
class BlackCardFilter:
    text: Optional[str] = None
    pick: Optional[int] = None

    def matches(self, card: BlackCard) -> bool:
        criteria = []

        if self.text is not None:
            criteria.append(self.text in card.text)

        if self.pick is not None:
            criteria.append(self.pick == card.pick)

        return all(criteria)


@strawberry.input
class WhiteCardFilter:
    text: Optional[str] = None

    def matches(self, card: WhiteCard) -> bool:
        criteria = []

        if self.text is not None:
            criteria.append(self.text.casefold() in card.text.casefold())

        return all(criteria)


@strawberry.input
class PackFilter:
    name: Optional[str] = None
    id: Optional[int] = None

    def matches(self, pack: Pack) -> bool:
        criteria = []

        if self.name is not None:
            criteria.append(self.name.casefold() in pack.name.casefold())

        if self.id is not None:
            criteria.append(self.id == pack.id)

        return all(criteria)
