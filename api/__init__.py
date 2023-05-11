import sys
from pathlib import Path

import ujson as json

here = Path(__file__).parent

paths = [
    here / "v1",
    here / "v2",
    here / "graphql",
]

sys.path.extend([str(p) for p in paths])

CAH = json.load((here / "cards.json").open())
