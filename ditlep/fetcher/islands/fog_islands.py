from pydantic import validate_arguments

from .base import IslandBaseFetcher

class FogIslandsFetcher(IslandBaseFetcher):
    __url = "https://www.ditlep.com/FogIsland/Get"

    @validate_arguments
    def __init__(self, id: int | None = None) -> None:
        super().__init__(self.__url, id)

__all__ = [ FogIslandsFetcher ]