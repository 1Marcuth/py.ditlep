from pydantic import validate_arguments

from ..base import BaseFetcher

class IslandBaseFetcher(BaseFetcher):
    @validate_arguments
    def __init__(
        self,
        url: str,
        id: int | None = None
    ) -> None:
        params = { "id": id }
        super().__init__(url, params)

__all__ = [ IslandBaseFetcher ]