from typing import Optional

import strawberry

__all__ = ["PackInput", "BlackCardInput", "WhiteCardInput"]


@strawberry.input
class BlackCardInput:
    text: Optional[str] = None
    pick: Optional[int] = None


@strawberry.input
class WhiteCardInput:
    text: Optional[str] = None


@strawberry.input
class PackInput:
    name: Optional[str] = None
    id: Optional[int] = None
