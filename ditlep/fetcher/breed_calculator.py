from pydantic import validate_arguments

from .base import BaseFetcher

class BreedCalculatorFetcher(BaseFetcher):
    __url = "https://www.ditlep.com/Breeding/CalculateNewBreeding"

    @validate_arguments
    def __init__(self, parent_ids: tuple[int, int]) -> None:
        params = {
            "parent1Id": parent_ids[0],
            "parent2Id": parent_ids[1]
        }

        super().__init__(self.__url, params)

__all__ = [ BreedCalculatorFetcher ]