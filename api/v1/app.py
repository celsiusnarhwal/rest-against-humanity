import urllib.parse
from pathlib import Path

import ujson as json
from fastapi import APIRouter, HTTPException

v1 = APIRouter(prefix="/api/v1")

cards_path = Path(__file__).parent.parent.joinpath("cards.json")


@v1.get("/")
async def get_packs(packs: str = None):
    cards_json = json.load(cards_path.open())

    if packs:
        packs = urllib.parse.unquote_plus(packs).split(",")
        if all(p in [pk["name"] for pk in cards_json] for p in packs):
            selected_packs = [p for p in cards_json if p["name"] in packs]

            black = []
            white = []

            for pack in selected_packs:
                for card in pack["white"]:
                    white.append(card["text"])

                for card in pack["black"]:
                    card.pop("pack")
                    black.append(card)

            return {"white": white, "black": black}
        else:
            raise HTTPException(
                status_code=400,
                detail="Your request included one or more invalid pack names",
            )
    else:
        return [p["name"] for p in cards_json]
