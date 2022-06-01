import json

from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def get_packs(packs: str = None):
    cards_json = json.load(open("cards.json"))

    if packs:
        valid_packs = [p["name"] for p in cards_json]
        if not any(p not in valid_packs for p in packs.split(",")):
            selected_packs = [p for p in cards_json if p["name"] in packs.split(",")]

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
            return {"error": "Your request included one or more invalid pack names"}
    else:
        return [p["name"] for p in cards_json]


handler = Mangum(app)
