from enum import Enum
from pathlib import Path
from typing import Any

import ujson as json
from fastapi import HTTPException
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, validator
from typing_extensions import Self

__all__ = ["Query", "BlackCard", "Deck", "WhiteCard"]

cards_path = Path(__file__).parent.parent.joinpath("cards.json")

cards = json.load(cards_path.open())
pack_names = [p["name"] for p in cards]


class Color(str, Enum):
    BLACK = "black"
    WHITE = "white"


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = "ignore"


class Query(BaseModel):
    packs: list[str] = Field(default_factory=lambda: pack_names.copy())
    color: Color = None
    pick: int = Field(default=None, ge=1, le=2)
    include_pack_names: bool = Field(default=True, alias="includePackNames")

    @validator("packs")
    def validate_packs(cls, v):
        if invaid := [p for p in v if p not in pack_names]:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid pack names: {', '.join(invaid)}",
            )

        return v


class WhiteCard(BaseModel):
    text: str
    pack_id: int = Field(alias="pack", exclude=True)
    pack: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack = pack_names[self.pack_id]

    def apply_query(self, query: Query) -> Self:
        if not query.include_pack_names:
            self.pack = None

        return self

    def __str__(self):
        return self.text


class BlackCard(WhiteCard):
    pick: int

    def apply_query(self, query: Query):
        if query.pick is not None and query.pick != self.pick:
            return None

        return super().apply_query(query)


class Deck(BaseModel):
    black: list[BlackCard]
    white: list[WhiteCard]

    def apply_query(self, query: Query) -> Self:
        if query.color is Color.BLACK:
            self.white = None
        elif query.color is Color.WHITE:
            self.black = None

        if self.black is not None:
            for index, card in enumerate(self.black):
                if (applied := card.apply_query(query)) is not None:
                    self.black[index] = applied
                else:
                    self.black.pop(index)

        if self.white is not None:
            for index, card in enumerate(self.white):
                if (applied := card.apply_query(query)) is not None:
                    self.white[index] = applied
                else:
                    self.white.pop(index)

        if self.black is None and self.white is None:
            return None

        return self

    # noinspection PyMethodOverriding
    @classmethod
    def parse_obj(cls: type, obj: Any, *, query: Query):
        parsed: Deck = super().parse_obj(obj)
        parsed = parsed.apply_query(query)

        return parsed
