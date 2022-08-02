import json
import urllib.parse

from fastapi import FastAPI, HTTPException
import os

app = FastAPI()


@app.get("/api")
async def get_packs(packs: str = None):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    cards_json = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards.json")))

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
            raise HTTPException(status_code=400, detail="Your request included one or more invalid pack names")
    else:
        return [p["name"] for p in cards_json]
