from pydantic import validate_arguments

from .base import BaseFetcher

class ItemsSearchFetcher(BaseFetcher):
    __url = "https://www.ditlep.com/Items/ItemFilter"

    @validate_arguments
    def __init__(
        self,
        id_or_name: str | int = "",
        sort: str = "",
        page_number: int | str = 1,
        page_size: int = 20,
        group: str = "",
    ) -> None:
        params = {
            "sort": sort,
            "page": page_number,
            "pageSize": page_size,
            "group": group,
            "filter": f"TypeId~eq~'{id_or_name}'~or~Name~contains~'{id_or_name}'~or~BuildingTime~contains~'{id_or_name}'~or~Price~contains~'{id_or_name}'~or~Sell~contains~'{id_or_name}'~or~InStore~contains~'{id_or_name}'"
        }

        super().__init__(self.__url, params)

__all__ = [ ItemsSearchFetcher ]