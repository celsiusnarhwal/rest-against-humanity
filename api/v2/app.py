from pathlib import Path

import ujson as json
from fastapi import APIRouter
from fastapi.requests import Request

from .models import *

v2 = APIRouter(prefix="/api/v2")

cards_path = Path(__file__).parent.parent.joinpath("cards.json")


@v2.get("/packs")
async def get_packs():
    return [p["name"] for p in json.load(cards_path.open())]


@v2.get("/cards")
async def get_cards(request: Request):
    params = dict(request.query_params)
    if params.get("packs"):
        params["packs"] = params["packs"].split(",")

    query = Query.parse_obj(params)

    packs = dict(packs=json.load(cards_path.open()))
    packs["packs"] = [p for p in packs["packs"] if p["name"] in query.packs]

    cards = dict(black=[], white=[])

    for pack in packs["packs"]:
        cards["black"].extend(pack["black"])
        cards["white"].extend(pack["white"])

    return Deck.parse_obj(cards, query=query).dict(exclude_none=True)
