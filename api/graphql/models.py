from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, root_validator, validator

from api import CAH

__all__ = ["BlackCard", "WhiteCard", "Pack"]


class BaseModel(PydanticBaseModel):
    class Config:
        extra = "ignore"


class WhiteCard(BaseModel):
    text: str = Field(description="The text of the card.")
    pack: Pack = Field(description="The pack the card belongs to.")

    # noinspection PyMethodParameters
    @root_validator(pre=True)
    def set_pack(cls, values):
        if type(values["pack"]) is not Pack:
            pack = Pack.construct(**CAH[values["pack"]])
            pack.id = values["pack"]
            return {**values, "pack": pack}

        return values


class BlackCard(WhiteCard):
    pick: int = Field(description="The number of blank spaces the card has.")


class Pack(BaseModel):
    name: str = Field(description="The name of the pack.")
    id: int = Field(None, description="The pack's unique identifier.")
    black: list[BlackCard] = Field(description="The pack's black cards.")
    white: list[WhiteCard] = Field(description="The pack's white cards.")

    # noinspection PyMethodParameters
    @validator("id", always=True)
    def set_id(cls, _, values):
        return CAH.index(next(p for p in CAH if p["name"] == values["name"]))


BlackCard.update_forward_refs()
WhiteCard.update_forward_refs()
