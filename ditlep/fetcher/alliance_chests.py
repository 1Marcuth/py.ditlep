from pydantic import validate_arguments
from datetime import datetime

from .base import BaseFetcher

class AllianceChestFetcher(BaseFetcher):
    __url = f"https://www.ditlep.com/AllianceChest/Get"

    @validate_arguments
    def __init__(self, month: int = datetime.now().month) -> None:
        params = { "month": month }
        super().__init__(self.__url, params)

__all__ = [ AllianceChestFetcher ]