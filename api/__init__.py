import sys
from pathlib import Path

here = Path(__file__).parent

paths = [
    here / "v1",
    here / "v2",
]

sys.path.extend([str(p) for p in paths])

cards_path = here.joinpath("cards.json")
