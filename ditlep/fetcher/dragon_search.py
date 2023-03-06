from pydantic import validate_arguments
import math

from .base import BaseFetcher, BaseAsyncFetcher

class DragonSearchFetcher(BaseFetcher):
    __url = "https://www.ditlep.com/Dragon/Search"

    @validate_arguments
    def __init__(
        self,
        name_or_id: str | int = "",
        rarities: list[str] = [],
        elements: list[str] = [],
        page_number: int = 0,
        page_size: int = 20,
        category: int | str = "",
        in_store: bool | None = None,
        is_breedable: bool | None = None,
        tag: str = ""
    ) -> None:

        params = {
            "dragonName": name_or_id,
            "rarities": rarities,
            "elements": elements,
            "page": page_number,
            "pageSize": page_size,
            "category": category,
            "inStore": in_store,
            "breedable": is_breedable,
            "tag": tag
        }

        super().__init__(self.__url, params)

class DragonSearchAsyncFetcher(BaseAsyncFetcher):
    __url = "https://www.ditlep.com/Dragon/Search"

    @validate_arguments
    def __init__(
        self,
        name_or_id: str | int = "",
        rarities: list[str] = [],
        elements: list[str] = [],
        page_number: int = 0,
        page_size: int = 20,
        category: int | str = "",
        in_store: bool | None = None,
        is_breedable: bool | None = None,
        tag: str = ""
    ) -> None:

        params = {
            "dragonName": name_or_id,
            "rarities": rarities,
            "elements": elements,
            "page": page_number,
            "pageSize": page_size,
            "category": category,
            "inStore": in_store,
            "breedable": is_breedable,
            "tag": tag
        }

        result = DragonSearchFetcher(
            name_or_id,
            rarities,
            elements,
            page_number,
            page_size,
            category,
            in_store,
            is_breedable,
            tag
        ).get()

        total_of_dragons: int = result["total"]
        total_of_pages = math.ceil(total_of_dragons / page_size)

        self.__results = { "items": result["items"], "total": total_of_dragons }

        urls_params = [
            (self.__url, {
                "dragonName": name_or_id,
                "rarities": rarities,
                "elements": elements,
                "page": new_page_number,
                "pageSize": page_size,
                "category": category,
                "inStore": in_store,
                "breedable": is_breedable,
                "tag": tag
            }) for new_page_number in range(1, total_of_pages)
        ]

        super().__init__(urls_params)

    def run(self):
        results = super().run()
        
        for result in results:
            self.__results["items"].extend(result["items"])

        return self.__results

__all__ = [ DragonSearchFetcher ]